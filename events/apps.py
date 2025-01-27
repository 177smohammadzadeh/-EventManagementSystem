from django.apps import AppConfig


class EventsConfig(AppConfig):
    """
    Configures the Events app.
    Sets the app name to 'events' and uses BigAutoField as the default primary key type.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'
