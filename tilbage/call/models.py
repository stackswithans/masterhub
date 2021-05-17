from django.db import models


class Call(models.Model):
    user = models.EmailField(max_length=50)
    callId = models.CharField(unique=True, max_length=32)
    participants = models.IntegerField()
