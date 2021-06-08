from django.urls import path, include
from .views import users


urlpatterns = [path("users/", users)]
