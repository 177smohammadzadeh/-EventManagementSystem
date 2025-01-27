from django.apps import AppConfig

class NotificationsConfig(AppConfig):
    """
    Configures the Notifications app.
    This class ensures the app is properly set up and integrates
    the necessary signals when the app is ready.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    def ready(self):
        import notifications.signals
        # Automatically imports signal handlers when the app is ready