from django.utils.timezone import make_aware, localtime
from .models import Event
from datetime import date, timedelta
from .forms import EventForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def home(request):
    """
    Shows a weekly planner with your events.
    - Gets all events and organizes them by date.
    - Only shows events for the next 7 days, starting from today.
    - Groups events by their date so you can easily see what’s coming up.
    """
    events = Event.objects.order_by('date')
    planner = {}
    start_date = date.today()
    end_date = start_date + timedelta(days=7)

    for single_date in (start_date + timedelta(days=n) for n in range((end_date - start_date).days + 1)):
        planner[single_date] = []

    for event in events:
        event_date = localtime(event.date).date()

        if event_date in planner:
            planner[event_date].append(event)

    return render(request, 'events/home.html', {'planner': planner})

def add_event(request):
    """
    Lets you add a new event to your planner.
    - If you visit this page (GET), it shows a form to fill out.
    - If you submit the form (POST), it checks the data, saves it,
        and makes sure the event date has the right timezone.
    """
    default_date = request.GET.get('date', None)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(commit=False)

            if not event.date.tzinfo:
                event.date = make_aware(event.date)

            event.save()
            return redirect('home')

    else:
        initial_data = {}

        if default_date:
            try:
                initial_data['date'] = make_aware(datetime.fromisoformat(default_date))

            except ValueError:
                pass
        form = EventForm(initial=initial_data)
    return render(request, 'events/add_event.html', {'form': form, 'date': default_date})

def delete_event(request, event_id):
    """
    Deletes an event based on its ID.
    - If the event exists and the request is valid, it gets deleted.
    - If the event doesn’t exist or there’s an error, it sends an error message.
    """
    if request.method == "DELETE":

        try:
            event = Event.objects.get(id=event_id)
            event.delete()
            return JsonResponse({"success": True}, status=200)

        except Event.DoesNotExist:
            return JsonResponse({"error": "Event not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)

def event_detail(request, event_id):
    """
    Shows details about a specific event.
    - Finds the event using its ID.
    - If the event isn’t found, you’ll get a 404 error page.
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def edit_event(request, event_id):
    """
    Lets you edit an existing event.
    - If you open the page (GET), it shows the current event details in a form.
    - If you submit the form (POST), it updates the event with the new data.
    """
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)

    else:
        form = EventForm(instance=event)

    return render(request, 'events/edit_event.html', {'form': form, 'event': event})
