from django.urls import path
from rest_framework.routers import SimpleRouter
import call.views as views


urlpatterns = [
    path("", views.call_create, name="call-calls"),
    path("<str:call_id>", views.call_join),
]
