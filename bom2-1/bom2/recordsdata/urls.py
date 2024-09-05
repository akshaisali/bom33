# urls.py
from django.urls import path
from . import views
from .views import get_equipment_data, get_front_conveyor_data, get_furnace_data, get_rear_conveyor_data
from .views import filter_data


urlpatterns = [
    path('',views.home, name='home'),  # Handle root URL
    path('form/<str:equipment_type>/', views.equipment_form_view, name='equipment_form'),
    path('success/', views.success_view, name='success'),
    path('add-data/', views.add_data_view, name='add_data'),
    path('get_furnace_data/', get_furnace_data, name='get_furnace_data'),
    path('get_front_conveyor_data/', get_front_conveyor_data, name='get_front_conveyor_data'),
    path('get-equipment-data/', views.get_equipment_data, name='get_equipment_data'),
    path('', filter_data, name='filter_data'),
    path('get_rear_conveyor_data/',get_rear_conveyor_data, name='get_rear_conveyor_data'),
]


