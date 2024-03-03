from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from watcheck.accounts.forms import RegisterForm, LoginForm
from watcheck.accounts.models import Account


# Create your views here.

class RegisterView(CreateView):
    model = Account
    form_class = RegisterForm
    template_name = 'account/sign-up.html'
    success_url = reverse_lazy('sign_in')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'account/sign-in.html'
    next_page = reverse_lazy('home')


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


def profile_details(request):
    return render(request, template_name='account/account-details.html')