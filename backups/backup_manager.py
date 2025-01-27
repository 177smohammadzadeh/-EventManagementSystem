import os
from datetime import datetime
from django.conf import settings
from .models import BackupFile

def create_backup():
    """
    Creates a backup of the database and stores it in a structured directory.
    - Creates a 'backups' folder in the project directory if it doesn't exist.
    - Organizes backups into subfolders by date (e.g., 'backups/2025-01-20/').
    - Names each backup file with a timestamp (e.g., 'backup_12-30-00.sqlite3').
    - Updates the BackupFile model with the relative path of the backup file.
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
        BackupFile.objects.create(file_path=os.path.relpath(backup_file, os.path.join(settings.BASE_DIR, 'backups')))
        return backup_file

    else:

        raise FileNotFoundError(f"Database file not found at {database_path}")


