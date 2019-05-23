from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Service(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)

class CustomUser(AbstractUser):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    is_client = models.BooleanField('client status', default=True)
    is_worker = models.BooleanField('worker status', default=False)

    def __str__(self):
        return self.email

class Proyect(models.Model):
    client = models.ForeignKey(CustomUser, related_name="cliente_user",  on_delete=models.CASCADE)
    worker = models.ForeignKey(CustomUser, related_name="worker_user",  on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.title
