from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
   pass

   def get_token(self):
        obj, created = Token.objects.get_or_create(user=self)
        return obj.key

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

