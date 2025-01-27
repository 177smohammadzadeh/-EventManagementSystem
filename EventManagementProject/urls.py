from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from events import views

"""
Defines the main URL patterns for the project.

- 'admin/': Provides access to the Django admin panel.
- '': Includes all URL patterns for the 'events' app (homepage and related views).
- 'add_event/': Directly maps to the 'add_event' view in the 'events' app.
- 'users/': Includes URL patterns for user-related functionality (login, register, etc.).
- 'backups/': Includes URL patterns for managing database backups.
- Serves media files in development mode when DEBUG is True.
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('add_event/', views.add_event, name='add_event'),
    path('users/', include('users.urls')),
    path('backups/', include('backups.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)