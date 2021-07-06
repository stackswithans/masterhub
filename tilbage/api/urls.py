from django.urls import path, include
from .views import routes, users, sessions


urlpatterns = [
    path("", routes),
    path("users/", users, name="api-users"),
    path("sessions/", sessions, name="api-sessions"),
]
