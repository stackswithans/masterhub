import uuid
from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from call.models import Call

# Create your views here.
@api_view(http_method_names=["POST"])
@parser_classes([JSONParser])
def call_create(request):
    user = request.data.get("user")
    renderer = JSONRenderer()
    new_call = Call.objects.create(
        user=user, callId=uuid.uuid4().hex, participants=0
    )
    new_call.save()
    return Response(renderer.render({"callId": new_call.callId}))


# Create your views here.
@api_view(http_method_names=["GET"])
@parser_classes([JSONParser])
def call_join(request, call_id):
    call = Call.objects.filter(callId=call_id)
    renderer = JSONRenderer()
    if not call.exists():
        return Response(
            renderer.render({"message": "Call does not exist"}, status=404)
        )
    call = call[0]
    return Response(
        renderer.render(
            {
                "user": call.user,
                "callId": call.callId,
            }
        )
    )
