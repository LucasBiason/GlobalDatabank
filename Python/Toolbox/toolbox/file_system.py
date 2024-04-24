import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage


def remove_file(file_path):
    try:
        path = os.path.join(settings.MEDIA_ROOT, file_path)
        os.remove(path)
        return True
    except Exception as msg:
        print(f"Error: {msg}")
        return False


def upload_tmp_file(file):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    uploaded_file_url = fs.path(filename)
    return uploaded_file_url


def remove_tmp_file(uploaded_file_url):
    try:
        os.remove(uploaded_file_url)
        return True
    except Exception as msg:
        print(f"Error: {msg}")
        return False
