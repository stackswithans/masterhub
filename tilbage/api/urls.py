from django.urls import path, include
from .views import routes, users, sessions, register_info


urlpatterns = [
    path("", routes),
    path("users/", users, name="api-users"),
    path("users/register_info/", register_info, name="api-registerinfo"),
    path("sessions/", sessions, name="api-sessions"),
]
