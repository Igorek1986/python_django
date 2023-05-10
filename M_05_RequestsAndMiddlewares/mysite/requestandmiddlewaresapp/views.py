from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def handle_file_upload_limit(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.FILES.get("myfile"):
        myfile = request.FILES["myfile"]
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        if request.FILES.get("myfile").size > 1048576:
            return render(request, "requestandmiddlewaresapp/error_upload.html")
    return render(request, "requestandmiddlewaresapp/file-upload.html")
    # else:
    # return render(request, "requestandmiddlewaresapp/error_upload.html")
