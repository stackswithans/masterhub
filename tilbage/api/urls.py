from django.urls import path, include
from .views import users, sessions


urlpatterns = [
    path("users/", users),
    path("sessions/", sessions),
]
