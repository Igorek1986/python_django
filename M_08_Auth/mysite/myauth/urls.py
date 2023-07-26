from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, reverse_lazy

from .views import (
    # MyLoginView,
    # MyLogoutView,
    get_cookie,
    set_cookie,
    get_session,
    set_session,
)

app_name = "myauth"

urlpatterns = [
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
            next_page=reverse_lazy(
                "myauth:login",
            ),
        ),
    ),
    path("cookie/get/", get_cookie, name="cookie-get"),
    path("cookie/set/", set_cookie, name="cookie-set"),
    path("session/get/", get_session, name="session-get"),
    path("session/set/", set_session, name="session-set"),
    # path("login/", MyLoginView.as_view(), name="login"),
    # path("logout/", MyLogoutView.as_view(), name="logout"),
]
