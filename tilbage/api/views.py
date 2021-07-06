import uuid
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, MasterSerializer, SessionSerializer
from .models import MasterhubUser, Master, KnowledgeCategory
from functools import reduce


# Returns the available api endpoints
@api_view(http_method_names=["GET"])
def routes(request):
    socket_protocol = "wss://" if request.is_secure() else "ws://"
    host = request.get_host()
    return Response(
        data={
            "users": request.build_absolute_uri(reverse("api-users")),
            "sessions": request.build_absolute_uri(reverse("api-sessions")),
            "calls": request.build_absolute_uri(reverse("call-calls")),
            "call_socket": f"{socket_protocol}{host}/ws/call",
        },
    )


@api_view(http_method_names=["GET"])
def register_info(request):

    # dict tuple into object
    degree = list(map(lambda d: {"id": d[0], "degree": d[1]}, Master.DEGREES))
    aois = list(
        map(
            lambda k: {"id": k.id, "description": k.description},
            KnowledgeCategory.objects.all(),
        )
    )
    print(degree, aois)

    return Response(
        data={"degree": degree, "aois": aois},
    )


@api_view(http_method_names=["POST", "DELETE"])
def sessions(request):
    if request.method == "POST":
        serializer = SessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = RefreshToken.for_user(user)
        return Response(
            {
                "email": user.email,
                "utype": serializer.validated_data["utype"],
                "name": f"{user.first_name} {user.last_name}",
                "access_token": str(token.access_token),
                "refresh_token": str(token),
            }
        )
    elif request.method == "DELETE":
        pass
    pass


@api_view(http_method_names=["POST"])
def users(request):
    # Validates the type of user that will be created
    # MS - Master / ST - Student
    print(request.data)
    if not request.data.get("utype"):
        raise serializers.ValidationError(
            ("utype", "This field must be provided")
        )
    if request.data["utype"] == MasterhubUser.STUDENT:
        serializer = UserSerializer(data=request.data)
    elif request.data["utype"] == MasterhubUser.MASTER:
        serializer = MasterSerializer(data=request.data)
    else:
        raise serializers.ValidationError(("utype", "Bad user type"))
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    token = RefreshToken.for_user(user.user)
    return Response(
        {
            "email": user.user.email,
            "utype": request.data["utype"],
            "name": f"{user.user.first_name} {user.user.last_name}",
            "access_token": str(token.access_token),
            "refresh_token": str(token),
        }
    )
