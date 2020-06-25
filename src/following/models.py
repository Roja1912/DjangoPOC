from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

class Following(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    following_id = models.PositiveIntegerField(blank=True, null=True)
    unfollow = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, editable=False)
