from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db import models

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(settings.MEDIA_URL, self.image)
        return '{}{}'.format(settings.STATIC_URL, 'img/empty.png')