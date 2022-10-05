from django.contrib.auth import get_user_model
from django.contrib.auth import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models.base import Model

class editprofileform(ModelForm):
    class Meta:
        model=User
        fields=("first_name","last_name", "email")
        labels={
                'first_name':'First name',
                'last_name':'last name',
                'email':'email',
        }