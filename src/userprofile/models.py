from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver



class Profiles(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, editable=False, on_delete=models.CASCADE, primary_key=True)
    profile = models.ImageField(upload_to='profiles/')
    blog = models.CharField(max_length=75, null=True)
    button_info = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, editable=False)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile_for_new_user(sender, created, instance, **kwargs):
#     if created:
#         profile = Profiles(user=instance  )
#         profile.save()

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile_for_new_user(sender, instance=None, created=False, **kwargs):
#     if created:
#         Profiles.objects.create(user=instance)

