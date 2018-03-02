from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField(default=timezone.now)

    # TODO: Data Name > what by same name?
    avatar = models.ImageField(upload_to='uploads/')
