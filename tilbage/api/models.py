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
    mh_user = models.OneToOneField(
        MasterhubUser,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )

    k_categories = models.ManyToManyField(
        "KnowledgeCategory",
    )

    job = models.ForeignKey(
        "Job",
        on_delete=models.CASCADE,
    )

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
    DAY_OF_WEEK = tuple(
        [(index, weekday) for index, weekday in enumerate(calendar.day_name)]
    )
    TIME_OF_DAY = tuple([(index, f"{index}:00") for index in range(6, 18)])

    day = models.IntegerField()
    time = models.IntegerField()


class KnowledgeCategory(models.Model):
    description = models.CharField(unique=True, max_length=100)


class Job(models.Model):
    description = models.CharField(unique=True, max_length=100)
