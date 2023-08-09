from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView


from .views import (
    AboutMeView,
)

app_name = "myauth"

urlpatterns = [
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path(
        "login/",
        LoginView.as_view(
            template_name="myauth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            next_page=reverse_lazy("myauth:login"),
        ),
        name="logout",
    ),
    path("register/", RegisterView.as_view(), name="register"),
]
