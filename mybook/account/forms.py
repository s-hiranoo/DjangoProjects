from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
