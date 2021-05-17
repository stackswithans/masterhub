import uuid
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(http_method_names=["POST"])
@parser_classes([JSONParser])
def new_call(request):
    user = request.data.get("user")
    renderer = JSONRenderer()
    return Response(renderer.render({"callId": uuid.uuid4().hex}))
