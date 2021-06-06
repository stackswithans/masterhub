from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MasterhubUser, Master


class UserSerializer(serializers.Serializer):
    utype = serializers.CharField(max_length=2)  # MS or ST
    first_name = serializers.CharField(required=True, max_length=100)
    last_name = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    gender = serializers.IntegerField(required=True)
    telephone = serializers.CharField(required=True, max_length=100)

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
