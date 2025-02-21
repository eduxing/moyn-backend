''' Models for the communities app '''
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Community(models.Model):
    ''' Model for a community of users '''
    members = models.ManyToManyField(get_user_model(), related_name='communities')
    admins = models.ManyToManyField(get_user_model(), related_name='admin_communities')
    title = models.CharField(max_length=255)
    handle = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    keywords = models.JSONField(default=list)  # Requires Django 3.1+
    active = models.BooleanField(default=True)
    private = models.BooleanField(default=False)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    members_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

class ContentModel(models.Model):
    ''' Abstract model for content with an author '''
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(ContentModel):
    ''' Model for a post in a community '''
    TRUSTWORTHINESS_CHOICES = [
        ('unchecked', 'Unchecked'),
        ('trustworthy', 'Trustworthy'),
        ('missing_context', 'Missing Context'),
        ('inaccurate', 'Inaccurate'),
    ]

    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    trustworthiness = models.CharField(max_length=20, choices=TRUSTWORTHINESS_CHOICES, default='unchecked')

    def __str__(self):
        return str(self.title)

class Comment(ContentModel):
    ''' Model for a comment on a post or another comment '''
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    comment = models.TextField()

    def __str__(self):
        return f'Comment by {self.author} on {self.content_object}'

class Reaction(models.Model):
    ''' Model for a reaction to a post or comment '''
    REACTION_CHOICES = [
        ('upvote', 'Upvote'),
        ('downvote', 'Downvote'),
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reaction = models.CharField(max_length=8, choices=REACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.reaction} by {self.author} on {self.content_object}'