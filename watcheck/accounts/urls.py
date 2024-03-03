from django.urls import path, include
from watcheck.accounts import views

urlpatterns = [
    path('sign_in/', views.LoginView.as_view(), name='sign_in'),
    path('sign_up/', views.RegisterView.as_view(), name='sign_up'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('account_details/', views.profile_details, name='account-details')
]
