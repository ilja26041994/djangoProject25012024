from django.urls import path
from . import views

urlpatterns = [
    path('initialaze/', views.initialaze, name='initialaze'),
]