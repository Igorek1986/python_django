from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy


# class MyLoginView(LoginView):
#     template_name = "myauth/login.html"
#     redirect_authenticated_user = True
#
#
# class MyLogoutView(LogoutView):
#     next_page = reverse_lazy("myauth:login")


def get_cookie(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "defalut_value")
    return HttpResponse(f"Cookie value: {value!r}")


def set_cookie(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_session(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "defaulf value")
    return HttpResponse(f"Session Value {value!r}")


def set_session(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set")
