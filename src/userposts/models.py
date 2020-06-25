from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver



class UserPosts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    postimage = models.ImageField(upload_to='postimages/')
    caption = models.CharField(max_length=400, null=True)
    likes = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, editable=False)


