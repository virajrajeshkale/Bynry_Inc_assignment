# customer/models.py

from django.conf import settings  
from django.db import models
from base.models import CustomUser

class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    description = models.TextField()  # Description field for the request
    file = models.FileField(upload_to='service_requests/', null=True, blank=True)  # Optional file field
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Service Request #{self.id} - {self.status}"
