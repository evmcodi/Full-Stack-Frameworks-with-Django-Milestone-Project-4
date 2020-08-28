from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_definitionssoftware, name='view_definitionssoftware'),
    path('create/', views.term_create, name='term_create'),
    path('update/<pk>/', views.term_update, name='term_update'),
    path('delete/<pk>/', views.term_delete, name='term_delete'),

]
