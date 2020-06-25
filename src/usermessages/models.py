from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from userposts.models import UserPosts

class UserMessages(models.Model):
    messagefrom = models.PositiveIntegerField(blank=True, null=True)
    messageto = models.PositiveIntegerField(blank=True, null=True)
    messagetext = models.CharField(max_length=2000, null=True)
    like_message = models.PositiveIntegerField(blank=True, null=True)
    remove_message = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, editable=False)
