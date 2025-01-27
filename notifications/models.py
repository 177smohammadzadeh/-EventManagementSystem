from django.db import models
from events.models import Event

class Reminder(models.Model):
    """
    Represents a reminder linked to an event.
    This model tracks the event, reminder date, and its status (pending or sent).
    """
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='reminders',
    )
    # Links the reminder to an event. Deleting the event also deletes its reminders.

    date = models.DateField()
    # Specifies the date for the reminder.

    status = models.CharField(
        max_length=10,
        choices=[
            ('pending', 'Pending'),
            ('sent', 'Sent'),
        ],
        default='pending'
    )
    # Tracks whether the reminder is still pending or has been sent.


    def __str__(self):
        # Provides a readable string representation of the reminder.
        return f"Reminder for Event {self.event_id} on {self.date}"


