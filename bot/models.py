from django.db import models


class UserOfBot(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
