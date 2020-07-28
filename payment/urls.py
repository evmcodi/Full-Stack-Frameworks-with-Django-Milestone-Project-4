from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_payment, name='payment'),
    path('payment_success/',
         views.payment_success,
         name='payment_success'),
]
