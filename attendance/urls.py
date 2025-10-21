from django.urls import path
from .views import add_farmer, farmer_list

urlpatterns = [
    path('farmers/add/', add_farmer, name='add_farmer'),
    path('farmers/', farmer_list, name='farmer_list'),
]