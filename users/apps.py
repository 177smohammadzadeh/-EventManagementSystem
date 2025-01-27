from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuration for the 'users' app.
    Sets default primary key field type and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
