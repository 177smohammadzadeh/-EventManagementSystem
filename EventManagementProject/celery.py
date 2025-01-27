from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

"""
Celery configuration for the EventManagementProject.
- Initializes the Celery app with the project's settings.
- Uses `django_celery_beat` for periodic task scheduling.
- Automatically discovers tasks defined in installed apps.
"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventManagementProject.settings')

app = Celery('EventManagementProject')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')