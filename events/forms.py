from django import forms
from django.utils.timezone import make_aware
from .models import Event

class EventForm(forms.ModelForm):
    """
    A form for creating and editing Event objects.

    - Fields included: title, description, date, and attachment.
    - Custom widgets:
      - Date field uses a datetime-local input for better user experience.
      - Description field uses a textarea with customizable size.
    - Validates the date field to ensure timezone awareness.
    """
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'attachment']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if not date.tzinfo:
            date = make_aware(date)
        return date
