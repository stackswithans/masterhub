from django.urls import path
from rest_framework.routers import SimpleRouter
import call.views as views


urlpatterns = [path("", views.new_call)]
