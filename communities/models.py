from django.db import models
from django.contrib.auth import get_user_model

class Community(models.Model):
    members = models.ManyToManyField(get_user_model(), related_name='communities')
    admins = models.ManyToManyField(get_user_model(), related_name='admin_communities')
    title = models.CharField(max_length=255)
    handle = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    keywords = models.JSONField(default=list)  # Requires Django 3.1+
    active = models.BooleanField(default=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title