import calendar
from django.db import models
from django.contrib.auth.models import User


class MasterhubUser(models.Model):
    GENDER = (("M", "Male"), ("F", "Female"), ("U", "UNKNOWN"))
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE
    )
    telephone = models.CharField(unique=True, max_length=100)


class Master(MasterhubUser):

    BACHELOR = 0
    MASTERS = 1
    DOCTORATE = 2
    NONE = 3
    DEGREES = (
        (BACHELOR, "Licenciatura"),
        (MASTERS, "Mestrado"),
        (DOCTORATE, "Doutoramento"),
        (NONE, "Nenhum"),
    )

    mh_user = models.OneToOneField(
        MasterhubUser,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )
    k_categories = models.ManyToManyField(
        "KnowledgeCategory",
    )
    job = models.CharField(
        max_length=100,
    )
    academic_degree = models.IntegerField(default=NONE, choices=DEGREES)
    timeslots = models.ManyToManyField("Timeslot")


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    master = models.ForeignKey(
        "Master", related_name="lesson_owner", on_delete=models.CASCADE
    )
    timeslot = models.ForeignKey("Timeslot", on_delete=models.CASCADE)
    users = models.ManyToManyField("MasterhubUser", related_name="lesson_users")

    class Meta:
        unique_together = [["title", "master"]]


class Timeslot(models.Model):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    DAY_OF_WEEK = (
        (MONDAY, "Mon"),
        (TUESDAY, "Tues"),
        (WEDNESDAY, "Wed"),
        (THURSDAY, "Thur"),
        (FRIDAY, "Fri"),
        (SATURDAY, "Sat"),
        (SUNDAY, "Sun"),
    )

    TIME_OF_DAY = tuple([(index, f"{index}:00") for index in range(6, 18 + 1)])

    day = models.IntegerField(choices=DAY_OF_WEEK)
    time = models.IntegerField(choices=TIME_OF_DAY)


class KnowledgeCategory(models.Model):
    description = models.CharField(unique=True, max_length=100)
