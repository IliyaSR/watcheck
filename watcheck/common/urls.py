from django.urls import path, include

from watcheck.common import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stores/', views.stores, name='stores'),
    path('search/', views.search_view, name='search'),
    path('bag/', views.bag_view, name='bag')
]
