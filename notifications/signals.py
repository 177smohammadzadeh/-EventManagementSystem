from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from .models import Reminder
from events.models import Event

@receiver(post_save, sender=Event)
def create_reminder_for_event(sender, instance, created, **kwargs):
    """
    Signal to automatically create a reminder when a new Event is created.

    This function listens to the `post_save` signal for the Event model.
    If a new Event instance is created, it generates a Reminder for that event
    with a default status of 'pending' and a date set to one day before the event's date.
    """
    if created:
        Reminder.objects.create(
            event=instance,
            date=instance.date - timedelta(days=1),
            status='pending'
        )