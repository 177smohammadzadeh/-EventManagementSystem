
from django.http import JsonResponse
from .tasks import backup_database
from django.http import HttpResponse, FileResponse,Http404
from .models import BackupFile
import os
from .backup_manager import create_backup
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

def backup_database_view(request):
    """
    Handles a request to trigger a database backup asynchronously.
     - If the request method is GET:
            - Calls the `backup_database` task using Celery.
            - Returns a JSON response indicating success or failure.
        - For non-GET requests:
            - Returns an error JSON response with a 405 status code.
        """
    if request.method == 'GET':
        try:
            task = backup_database.delay()
            return JsonResponse({'status': 'success'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Backup failed.'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)

def list_backups(request):
    """
    Displays a list of all available backups.
    - Fetches backup records from the `BackupFile` model, ordered by creation date.
    - Checks if the corresponding backup files exist and filters valid ones.
    - Passes the list of valid backups to the `list_backups.html` template.
    """
    backups = BackupFile.objects.all().order_by('-created_at')
    backup_list = []

    for backup in backups:
        full_path = os.path.join(settings.BASE_DIR, 'backups', backup.file_path)

        if os.path.exists(full_path) and full_path.endswith('.sqlite3'):
            backup_list.append({
                'created_at': backup.created_at,
                'file_name': os.path.basename(backup.file_path),
                'file_path': backup.file_path,
            })
    return render(request, 'backups/list_backups.html', {'backups': backup_list})

def download_backup(request, file_path):
    """
    Handles downloading a specific backup file.
    - Constructs the full file path using the provided relative `file_path`.
    - If the file exists:
        - Returns the file as a downloadable attachment.
    - If the file does not exist:
        - Raises a 404 error.
        """
    file_full_path = os.path.join(settings.BASE_DIR, 'backups', file_path)

    if os.path.exists(file_full_path):
        return FileResponse(open(file_full_path, 'rb'), as_attachment=True, filename=os.path.basename(file_full_path))

    else:
        raise Http404("File not found")

def create_backup_view(request):
    """
    Manually triggers the creation of a new database backup.
    - Calls the `create_backup` function to perform the backup process.
    - Adds a success or error message to the request context based on the outcome.
    - Redirects the user to the homepage.
    """
    try:
        create_backup()
        messages.success(request, "Backup created successfully!")

    except Exception as e:
        messages.error(request, f"Failed to create backup: {e}")

    return redirect('home')
