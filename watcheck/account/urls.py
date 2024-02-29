from django.urls import path, include
from watcheck.account import views


urlpatterns = [
    path('sign_in/', views.LoginView.as_view(), name='sign_in'),
    path('sign_up/', views.RegisterView.as_view(), name='sign_up')
]