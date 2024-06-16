from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_drivers, name='all_drivers'),
    ]
