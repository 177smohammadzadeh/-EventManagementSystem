from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import backup_database_view
import os

"""
Defines URL patterns for managing database backups.

- 'backup/': Triggers the database backup process.
- 'list/': Displays a list of available backups.
- 'download/<path:file_path>/': Downloads a specific backup file.
- 'createbackup/': Manually creates a new database backup.
- Serves static files under '/backups/' from the backups directory.
"""
urlpatterns = [
    path('backup/', backup_database_view, name='backup_database'),
    path('list/', views.list_backups, name='backup_list'),
    path('download/<path:file_path>/', views.download_backup, name='download_backup'),
    path('createbackup/', views.create_backup_view, name='create_backup'),
]
urlpatterns += static('/backups/', document_root=os.path.join(settings.BASE_DIR, 'backups'))