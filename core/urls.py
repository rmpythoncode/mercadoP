
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('add_card/', views.add_card, name='add_card'),

    path('card_token/', views.card_token, name='card_token'),

    path('create_customer/', views.create_customer,
         name='create_customer'),

    path('create_customer_js/', views.create_customer_js,
         name='create_customer_js'),
]
