from django.urls import path
from . import views

"""
Defines URL patterns for the Event app.

- '' (home): Displays the homepage with a list of events.
- 'add_event/': Provides a form for adding a new event.
- 'delete_event/<int:event_id>/': Deletes a specific event by its ID.
- 'event/<int:event_id>/': Shows details for a specific event.
- 'edit_event/<int:event_id>/': Provides a form to edit an existing event.
"""
urlpatterns = [
    path('', views.home, name='home'),
    path('add_event/', views.add_event, name='add_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
]