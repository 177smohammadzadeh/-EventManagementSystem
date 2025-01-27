from django.apps import AppConfig

class BackupsConfig(AppConfig):
    """
    Configures the Backup app.
    Sets the app name to 'backups'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backups'
