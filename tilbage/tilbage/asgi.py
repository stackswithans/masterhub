"""
ASGI config for tilbage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from dotenv import load_dotenv
from channels.http import AsgiHandler
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import lesson.routing

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tilbage.settings")
django.setup()
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(lesson.routing.websocket_urlpatterns),
    }
)
