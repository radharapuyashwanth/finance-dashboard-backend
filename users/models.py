from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_VIEWER = 'viewer'
    ROLE_ANALYST = 'analyst'
    ROLE_ADMIN = 'admin'

    ROLE_CHOICES = [
        (ROLE_VIEWER, 'Viewer'),
        (ROLE_ANALYST, 'Analyst'),
        (ROLE_ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_VIEWER)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.username} ({self.role})'
