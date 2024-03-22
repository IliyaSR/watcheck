from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

from watcheck.accounts.forms import RegisterForm, LoginForm, AddressForm, EditAccountForm, ChangePassword
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
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account-details', pk)
    else:
        form = EditAccountForm(instance=request.user)

        context = {
            'form': form,
        }

        return render(request, template_name='account/account-details.html', context=context)


def addresses(request, pk):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        user = Account.objects.get(pk=pk)
        if form.is_valid():
            address = form.save(commit=False)
            address.current_profile = user
            address.save()
            return redirect('account-details', pk)
    else:
        form = AddressForm()

        context = {
            'form': form
        }

        return render(request, template_name='account/shipping-addresses.html', context=context)


def orders(request, pk):
    return render(request, template_name='account/orders.html')


def returns(request, pk):
    return render(request, template_name='account/returns.html')


class MyPasswordChangeView(PasswordChangeView):
    form_class = ChangePassword
    template_name = 'account/change-password.html'

    def get_success_url(self):
        return reverse_lazy('account-details', kwargs={'pk': self.request.user.pk})
