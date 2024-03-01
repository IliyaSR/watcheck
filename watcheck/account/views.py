from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from watcheck.account.forms import UserForm, LoginForm
from watcheck.account.models import Account


# Create your views here.

class RegisterView(CreateView):
    model = Account
    form_class = UserForm
    template_name = 'account/sign-up.html'
    success_url = reverse_lazy('sign_in')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'account/sign-in.html'
    next_page = reverse_lazy('home')


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')
