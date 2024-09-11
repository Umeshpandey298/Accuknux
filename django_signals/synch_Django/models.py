from django.db import models
from django.conf import settings

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MyModel_2(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class MyModel_3(models.Model):
    name = models.CharField(max_length=100)

