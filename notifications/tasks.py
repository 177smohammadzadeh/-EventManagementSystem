from celery import shared_task
from django.utils.timezone import now
from .models import Reminder
from .utils import send_event_reminders
from django.contrib.auth.models import User

@shared_task
def process_reminders():
    """
    Celery task to process and send pending reminders for events.
    This task fetches all reminders that are due (date <= now) and have a
    status of 'pending'. For each reminder, it sends an email notification
    to all users with a valid email address and updates the reminder status
    to 'sent'. If an error occurs, it logs the failure.
    """
    reminders = Reminder.objects.filter(date__lte=now(), status='pending')
    # Fetch all reminders that are pending and scheduled for today or earlier

    for reminder in reminders:
        event = reminder.event
        try:
            # Get all user email addresses (non-empty, non-null)
            user_emails = User.objects.filter(email__isnull=False).exclude(email__exact='').values_list('email', flat=True)

            # Send reminder emails using the utility function
            send_event_reminders(
                event_title=event.title,
                event_date=event.date,
                event_description=event.description,
                user_emails=list(user_emails),
            )

            # Update the reminder status to 'sent' after successful email delivery
            reminder.status = 'sent'
            reminder.save()
        except Exception as e:
            print(f"Failed to send reminder for event {event.title}: {e}")

