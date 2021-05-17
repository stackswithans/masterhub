from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path(r"ws/lesson/", consumers.LessonConsumer.as_asgi()),
    path(r"ws/lesson/<slug:lesson_id>", consumers.LessonConsumer.as_asgi()),
]
