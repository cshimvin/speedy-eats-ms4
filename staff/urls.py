from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_drivers, name='all_drivers'),
    path('add/', views.add_driver, name='add_driver'),
    path('edit/<int:driver_id>/', views.edit_driver, name='edit_driver'),
    path('details/<int:driver_id>', views.driver_detail, name='driver_detail'),
    path('delete/<int:driver_id>/',
         views.delete_driver, name='delete_driver'),
    ]
