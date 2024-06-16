from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_drivers, name='all_drivers'),
    path('add/', views.add_driver, name='add_driver'),
    path('edit/<int:driver_id>/', views.edit_driver, name='edit_driver'),
    ]
