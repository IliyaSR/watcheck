from django.urls import path, include

from watcheck.common import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stores/', views.stores, name='stores'),
    path('search/', views.search_view, name='search'),
    path('bag/', views.bag_view, name='bag'),
    path('add_to_bag/<int:pk>/', views.add_to_bag_view, name='add_to_bag'),
    path('bag_remove_item/<int:pk>/', views.remove_item_from_bag, name='remove_item'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('guarantee/', views.guarantee, name='guarantee'),
    path('all_orders/', views.check_all_orders, name='all_orders'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('payment_options/', views.payment_options, name='payment_options'),
    path('shipping_policy/', views.shipping_policy, name='shipping_policy'),
    path('faq/', views.faq, name='faq')
]
