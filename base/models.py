from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    SUPPORT = 'support'
    USER_TYPE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SUPPORT, 'Support Agent'),
    ]
    
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=CUSTOMER,
    )

    # Fix reverse accessor conflict for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  # Custom reverse relation name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_set',  # Custom reverse relation name
        blank=True
    )

    def __str__(self):
        return self.username


