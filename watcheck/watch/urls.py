from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from watcheck.watch import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('watch_details/<int:pk>/', views.watch_details, name='watch_details')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)