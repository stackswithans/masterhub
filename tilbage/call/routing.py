from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r"ws/call/<str:call_id>", consumers.CallConsumer.as_asgi()),
]
