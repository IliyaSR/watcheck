from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

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


class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'account/shipping-addresses.html'

    def post(self, *args, pk):
        self.request.user.delete()
        return redirect('home')


def account_details(request, pk):
    current_account = Account.objects.get(pk=pk)
    context = {
        'current_account': current_account
    }
    return render(request, template_name='account/account-details.html', context=context)


def addresses(request, pk):
    return render(request, template_name='account/shipping-addresses.html')


def orders(request, pk):
    return render(request, template_name='account/orders.html')


def returns(request, pk):
    return render(request, template_name='account/returns.html')