from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .forms import UserCreateForm
from django.views.generic.edit import CreateView



def index(request):
    return HttpResponse('index page')


class SignUpView(CreateView):
    model = User
    # fields = ('username', 'password1', 'password2',)
    form_class = UserCreationForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')

