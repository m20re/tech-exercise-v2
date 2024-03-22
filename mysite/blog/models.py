from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models.functions import Lower

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Post(models.Model):
    """Model representing an online post"""
    title =  models.CharField(max_length=100)
    # only one unique username can exist at a time
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # if the user is deleted, remove everything else
        blank=True,
        null=True
    )
    description = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
# Create your models here.
