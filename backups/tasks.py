from celery import shared_task
import os
from datetime import datetime
from django.conf import settings
from .backup_manager import create_backup

@shared_task
def backup_database():
    """
      Creates a database backup.
      - Ensures a folder structure exists for backups.
      - Copies the database file (`db.sqlite3`) into a new backup file with a timestamp.
      - Stores the backup in a folder named with the current date.
      """
    backup_dir = os.path.join(settings.BASE_DIR, "backups")

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    date_folder = datetime.now().strftime("%Y-%m-%d")
    backup_folder = os.path.join(backup_dir, date_folder)

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    database_path = os.path.join(settings.BASE_DIR, "db.sqlite3")
    timestamp = datetime.now().strftime("%H-%M-%S")
    backup_file = os.path.join(backup_folder, f"backup_{timestamp}.sqlite3")

    if os.path.exists(database_path):
        os.system(f"cp {database_path} {backup_file}")
        return f"Backup created at: {backup_file}"

    else:
        return f"Database file not found at {database_path}"

@shared_task
def backup_database():
    """
    Creates a database backup using the `create_backup` function.
    - Delegates the backup process to `create_backup`.
    - Handles any errors (e.g., missing database file).
    """
    try:
        backup_file = create_backup()
        return f"Backup created at: {backup_file}"

    except FileNotFoundError as e:
        return str(e)