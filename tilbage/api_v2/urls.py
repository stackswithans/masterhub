from django.urls import path, include
from .views import (
    routes,
    users_masters,
    users_students,
    sessions,
    register_info,
)


urlpatterns = [
    path("", routes),
    path("users/students", users_students, name="apiv2-students"),
    path("users/masters", users_masters, name="apiv2-masters"),
    path(
        "users/masters/register_info/", register_info, name="apiv2-registerinfo"
    ),
    path("sessions/", sessions, name="apiv2-sessions"),
]
