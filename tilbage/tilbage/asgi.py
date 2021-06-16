"""
ASGI config for tilbage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django

django.setup()

from dotenv import load_dotenv
from channels.http import AsgiHandler
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
import call.routing
from call.consumers import CallConsumer

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tilbage.settings")
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(call.routing.websocket_urlpatterns),
        "channel": ChannelNameRouter({"call": CallConsumer.as_asgi()}),
    }
)
