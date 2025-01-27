from django.contrib import admin
from django.forms import ModelForm
from notifications.models import Reminder
from .models import Event
from django.forms.widgets import SplitDateTimeWidget

class EventAdminForm(ModelForm):
    """
    Custom form for the Event model in the admin panel.
    It uses SplitDateTimeWidget to separate date and time inputs.
    """
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': SplitDateTimeWidget(),
        }

class ReminderInline(admin.TabularInline):
    """
    Inline configuration for the Reminder model.
    Allows adding reminders directly from the Event admin page.
    """
    model = Reminder
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Customizes the Event model admin interface:
    - Uses SplitDateTimeWidget for the date field.
    - Displays title, date, description, and attachment in the list view.
    - Adds search by title and description, and a date filter.
    - Includes inline reminders for quick management.
    """
    form = EventAdminForm
    list_display = ('title', 'date', 'description', 'attachment')
    search_fields = ('title', 'description')
    list_filter = ('date',)
    inlines = [ReminderInline]