from django.urls import path
from . import views

urlpatterns = [
    path('initialaze/', views.initialaze, name='initialaze'),
    path('get-cars/', views.get_cars, name='get_cars'),
    path('get-car-by-id/<int:car_id>/', views.get_car_by_id, name='get_car_by_id'),
]