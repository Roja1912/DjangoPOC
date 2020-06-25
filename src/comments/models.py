from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from userposts.models import UserPosts

class Comments(models.Model):
    post = models.ForeignKey(UserPosts, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    comments = models.CharField(max_length=200, null=True)
    like_comments = models.PositiveIntegerField(blank=True, null=True)
    remove_comments = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, editable=False)
