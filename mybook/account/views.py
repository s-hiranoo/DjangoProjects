from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .forms import UserCreateForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
#from .models import *


class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'account/login.html'


class SignUpView(CreateView):
    model = User
    # fields = ('username', 'password1', 'password2',)
    form_class = UserCreateForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('account:login')


def CreateAccount(request):
    user = User()
    context = {}
    # POSTの時（新規であれ編集であれ登録ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = UserCreateForm(request.POST, instance=user)
        if form.is_valid():  # バリデーションがOKなら保存
            user = form.save(commit=False)
            user.save()
            user.groups.add(request.POST['role'])
            return redirect('account:login')
    else:  # GETの時（フォームを生成）
        form = UserCreateForm(instance=user)

    context['form'] = form
    return render(request, 'account/signup.html', context)
