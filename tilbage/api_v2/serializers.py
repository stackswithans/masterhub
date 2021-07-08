from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import MasterhubUser, Master, Timeslot, KnowledgeCategory

REQUIRED_ERR_MSG = "Este campo deve ser preenchido"
BAD_CREDS_MSG = "O e-mail e/ou  a palavra-passe estão incorrectos"
DEFAULT_ERRORS = {
    "blank": REQUIRED_ERR_MSG,
    "null": REQUIRED_ERR_MSG,
}


class SessionSerializer(serializers.Serializer):
    email = serializers.EmailField(
        error_messages={
            "invalid": "Este e-mail é inválido",
            **DEFAULT_ERRORS,
        }
    )
    password = serializers.CharField(error_messages=DEFAULT_ERRORS)

    def validate(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        print(user)
        if not user:
            raise serializers.ValidationError(
                {"email": BAD_CREDS_MSG, "password": BAD_CREDS_MSG}
            )
        utype = (
            MasterhubUser.MASTER
            if Master.objects.filter(user__email=data["email"])
            else MasterhubUser.STUDENT
        )
        return {"utype": utype, "user": user, **data}


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
    email = serializers.EmailField(
        error_messages={
            "invalid": "Este e-mail é inválido",
            **DEFAULT_ERRORS,
        }
    )
    password = serializers.CharField(error_messages=DEFAULT_ERRORS)
    gender = serializers.ChoiceField(
        MasterhubUser.GENDERS, error_messages=DEFAULT_ERRORS
    )
    telephone = serializers.CharField(
        max_length=9,
        error_messages=DEFAULT_ERRORS,
    )

    def create(self, validated_data):
        data = validated_data
        user = User.objects.create_user(
            data["email"],
            email=data["email"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data["last_name"],
        )

        mh_user = MasterhubUser.objects.create(
            user=user, gender=data["gender"], telephone=data["telephone"]
        )
        return mh_user

    def validate_email(self, value):
        user = User.objects.filter(username=value)
        if user:
            raise serializers.ValidationError(
                "Já existe um usuário com este e-mail", "email_exists"
            )
        return value

    def validate_telephone(self, value):
        user = MasterhubUser.objects.filter(telephone=value)
        if user:
            raise serializers.ValidationError(
                "Esse número de telefone já está registrado",
            )
        return value


class MasterSerializer(UserSerializer):
    occupation = serializers.CharField(
        max_length=100, error_messages=DEFAULT_ERRORS
    )
    timeslot = serializers.ListField(
        child=serializers.ListField(child=serializers.BooleanField()),
        error_messages=DEFAULT_ERRORS,
    )
    knowledge_areas = serializers.ListField(
        child=serializers.IntegerField(), error_messages=DEFAULT_ERRORS
    )
    academic_degree = serializers.ChoiceField(
        Master.DEGREES, error_messages=DEFAULT_ERRORS
    )

    def create(self, validated_data):
        data = validated_data
        user = User.objects.create_user(
            data["email"],
            email=data["email"],
            password=data["password"],
            first_name=data["first_name"],
            last_name=data["last_name"],
        )
        master = Master.objects.create(
            user=user,
            gender=data["gender"],
            telephone=data["telephone"],
            occupation=data["occupation"],
            academic_degree=data["academic_degree"],
        )
        # Get the selected time slots
        for h, hour in enumerate(data["timeslot"]):
            for d, day in enumerate(hour):
                if not day:
                    continue
                master.timeslots.add(Timeslot.objects.get(day=d, time=h + 6))
        # Add knowledge areas
        for area in data["knowledge_areas"]:
            master.k_categories.add(KnowledgeCategory.objects.get(pk=area))
        return master
