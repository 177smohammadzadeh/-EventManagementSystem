from django.db import models

class BackupFile(models.Model):
    """
    Model for storing backup file information.
    - Fields:
      - `created_at`: Automatically records the date and time when the backup is created.
      - `file_path`: Stores the file path of the backup (maximum length 255 characters).
    """
    created_at = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return f"Backup created at {self.created_at}"