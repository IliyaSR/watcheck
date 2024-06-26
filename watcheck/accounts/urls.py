from django.urls import path, include
from watcheck.accounts import views

urlpatterns = [
    path('sign_in/', views.LoginView.as_view(), name='sign_in'),
    path('sign_up/', views.RegisterView.as_view(), name='sign_up'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('details/', views.account_details, name='account-details'),
        path('addresses/', views.addresses, name='addresses'),
        path('delete_address/', views.delete_address, name='delete_address'),
        path('orders/', views.orders, name='orders'),
        path('delete/', views.AccountDeleteView.as_view(), name='account-delete'),
        path('change_password', views.MyPasswordChangeView.as_view(), name='change-password'),
    ]))
]
