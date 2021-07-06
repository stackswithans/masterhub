from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r"ws/call", consumers.CallConsumer.as_asgi(), name="call-wscall"),
]
