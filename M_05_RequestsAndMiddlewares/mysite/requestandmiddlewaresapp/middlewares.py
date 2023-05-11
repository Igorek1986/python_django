from django.http import HttpRequest
from django.utils.timezone import now
from .views import error_time_access


class ThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.throttle = {}

    def __call__(self, request: HttpRequest):
        user_ip = request.META["REMOTE_ADDR"]
        response = self.get_response(request)
        start = now()
        if user_ip in self.throttle:
            if round((start - self.throttle[user_ip]["start"]).total_seconds()) < 10:
                return error_time_access(request)
        self.throttle[user_ip] = {"start": start}
        return response
