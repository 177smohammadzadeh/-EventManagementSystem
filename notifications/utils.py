
from django.core.mail import send_mail

def send_event_reminders(event_title, event_date, event_description, user_emails):
    """
    Sends email reminders for an upcoming event.
    This function constructs an email with the event's details (title, date, description)
    and sends it to a list of user email addresses. If an error occurs during the process,
    it logs the exception for debugging purposes.
    """
    subject = f"Reminder: Upcoming Event - {event_title}"
    # Subject of the email, including the event title

    message = f"""
    Hi,
    This is a reminder for the upcoming event:

    Title: {event_title}
    Date: {event_date}
    Description: {event_description}

    Please let us know if you have any questions.
    """
    # Email body, containing event details

    try:
        send_mail(
            subject,
            message,
            'samaneh.mohammadzadeh88@gmail.com',
            user_emails,
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending email: {e}")