from django.urls import path, include

from watcheck.common import views

urlpatterns = [
    path('', views.home, name='home')
]