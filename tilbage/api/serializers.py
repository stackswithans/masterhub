from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MasterhubUser, Master

REQUIRED_ERR_MSG = "Este campo deve ser preenchido"
DEFAULT_ERRORS = {
    "blank": REQUIRED_ERR_MSG,
    "null": REQUIRED_ERR_MSG,
}


class UserSerializer(serializers.Serializer):
    utype = serializers.CharField(max_length=2)  # MS or ST
    first_name = serializers.CharField(
        max_length=100,
        error_messages=DEFAULT_ERRORS,
    )
    last_name = serializers.CharField(
        max_length=100,
        error_messages=DEFAULT_ERRORS,
    )
    email = serializers.EmailField(error_messages=DEFAULT_ERRORS)
    password = serializers.CharField(error_messages=DEFAULT_ERRORS)
    gender = serializers.IntegerField(error_messages=DEFAULT_ERRORS)
    telephone = serializers.CharField(
        max_length=9,
        error_messages=DEFAULT_ERRORS,
    )

    def create(self, validated_data):
        data = validated_data
        user = User.objects.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=data["email"],
            email=data["email"],
            password=data["password"],
        )

        mh_user = MasterhubUser.objects.create(
            user=user, gender=data["gender"], telephone=data["telephone"]
        )
        return mh_user


class MasterSerializer(UserSerializer):
    job = serializers.CharField(max_length=100)
    timeslot = serializers.CharField(max_length=100)
    # categories = None
    academic_degree = serializers.IntegerField()

    def create(self, validated_data):
        data = validated_data
        user = super().save()
        master = Master.objects.create(
            mh_user=user,
            job=data["job"],
            academic_degree=data["academic_degree"],
        )
        return mh_user
