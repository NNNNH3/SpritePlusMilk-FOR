from django import forms
from core import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserDisplayForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('patronymic', 'phone_number', 'date_of_birth')
