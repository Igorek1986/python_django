from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def handle_file_upload_limit(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.FILES.get("myfile"):
        myfile = request.FILES["myfile"]
        if request.FILES.get("myfile").size > 1048576:
            return render(request, "requestandmiddlewaresapp/error_upload.html")
        else:
            fs = FileSystemStorage()
            fs.save(myfile.name, myfile)
    return render(request, "requestandmiddlewaresapp/file-upload.html")


def error_time_access(request: HttpRequest) -> HttpResponse:
    return render(request, "requestandmiddlewaresapp/error-time.html")
