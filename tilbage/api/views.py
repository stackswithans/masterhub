import uuid
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, MasterSerializer


@api_view(http_method_names=["POST"])
def users(request):
    # Validates the type of user that will be created
    # MS - Master / ST - Student
    print(request.data)
    if not request.data.get("utype"):
        raise serializers.ValidationError(
            ("utype", "This field must be provided")
        )
    if request.data["utype"] == "ST":
        serializer = UserSerializer(data=request.data)
    elif request.data["utype"] == "MS":
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
            "access": str(token.access_token),
            "refresh": str(token),
        }
    )
