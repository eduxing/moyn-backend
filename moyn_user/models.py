from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MoynUser(AbstractUser):
    # Add custom fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username
