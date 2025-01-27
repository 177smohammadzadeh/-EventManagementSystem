from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    """
    This class customizes how the Reminder model shows up in the admin panel.
    It makes it easier for admins to view, filter, and search reminders
    by showing key fields like event, date, and status.
    """
    list_display = ('event', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('event__title',)