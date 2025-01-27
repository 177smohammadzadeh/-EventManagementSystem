from django_celery_beat.models import PeriodicTask, IntervalSchedule

"""
Sets up a periodic task to back up the database daily.
- Defines a schedule to repeat every 1 day.
- Creates a periodic task that runs the "backup_database" function daily, using the defined schedule.
"""
schedule, created = IntervalSchedule.objects.get_or_create(
    every=1,
    period=IntervalSchedule.DAYS,
)

PeriodicTask.objects.get_or_create(
    interval=schedule,
    name="Daily Database Backup",
    task="backups.tasks.backup_database",
)