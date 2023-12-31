from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DetailView,
)
from django.shortcuts import redirect, render

from .models import Profile
from .forms import ProfileUpdateForm


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.filter(user=self.request.user).first()
        context["user"] = self.request.user
        context["profile"] = profile
        return context

    def get(self, request):
        profile = request.user.profile
        form = ProfileUpdateForm(instance=profile)

        return render(
            request,
            self.template_name,
            {
                "form": form,
            },
        )

    def post(self, request: HttpRequest):
        profile = request.user.profile
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            user_bio = form.cleaned_data.get("bio")
            user_img_url = form.cleaned_data.get("avatar")
            profile = request.user.profile
            if user_bio:
                profile.bio = user_bio
            if user_img_url:
                profile.avatar = user_img_url
            profile.save()
        return redirect(request.path)


class AvatarUpdateView(UpdateView):
    template_name = "myauth/avatar_update.html"
    model = Profile
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse_lazy("myauth:about-me")


class UserDetailsView(DetailView):
    template_name = "myauth/user-detail.html"
    context_object_name = "user"
    model = User


class UserList(ListView):
    template_name = "myauth/user-list.html"
    context_object_name = "users"
    model = User


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value: {value!r}")


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "eggs"})
