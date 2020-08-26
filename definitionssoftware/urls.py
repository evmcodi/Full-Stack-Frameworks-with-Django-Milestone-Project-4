from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_definitionssoftware, name='view_definitionssoftware'),
    # path('add-term/', views.add_data, name='add_data'),
]
