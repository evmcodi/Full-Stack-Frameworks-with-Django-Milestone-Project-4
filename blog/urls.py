from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    # path('add/<item_id>/', views.add_to_blog, name='add_to_blog'),
    # path('adjust/<item_id>/', views.adjust_blog, name='adjust_blog'),
    # path('remove/<item_id>/', views.remove_from_blog, name='remove_from_blog'),
]
