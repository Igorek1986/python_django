from django.urls import path
from .views import handle_file_upload_limit

app_name = "requestandmiddlewaresapp"

urlpatterns = [
    path("upload/", handle_file_upload_limit, name="Upload"),
]
