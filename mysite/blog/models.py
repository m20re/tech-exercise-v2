from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
from  django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Post(models.Model):
    """Model representing an online post"""
    title =  models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
