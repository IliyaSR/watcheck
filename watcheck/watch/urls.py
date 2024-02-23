from django.urls import path, include

from watcheck.watch import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('watch_details/<int:pk>/', views.watch_details, name='watch_details')
]