from django.urls import path, include

from watcheck.common import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stores/', views.stores, name='stores'),
    path('search/', views.search_view, name='search'),
    path('bag/', views.bag_view, name='bag'),
    path('add_to_bag/<int:pk>/', views.add_to_bag_view, name='add_to_bag'),
    path('bag_remove_ite/<int:pk>/', views.remove_item_from_bag, name='remove_item'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
]
