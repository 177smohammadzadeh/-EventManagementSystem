from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """
    Model for representing events.

    - Fields:
      - title: The name of the event (max length 200 characters).
      - description: A detailed text description of the event.
      - date: The scheduled date and time for the event.
      - attachment: An optional file associated with the event, stored in 'uploads/'.
    - String representation returns the event title and date.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.date})"