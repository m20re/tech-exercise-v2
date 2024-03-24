from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from . import models

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = models.CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = models.CustomUser
        fields = ("username", "email")

class CreatePost(forms.ModelForm):

    class Meta:     
        model = models.Post
        fields = ['title', 'description', 'content']
