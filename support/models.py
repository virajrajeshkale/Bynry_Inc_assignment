from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from customer.models import ServiceRequest
from django.conf import settings

class SupportRepresentative(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class ServiceRequest(models.Model):
    assigned_to = models.ForeignKey(SupportRepresentative, null=True, blank=True, on_delete=models.SET_NULL)
