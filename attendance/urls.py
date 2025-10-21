from django.urls import path
from .views import add_farmer, mark_attendance, attendance_list, farmer_list_json

urlpatterns = [
    path('farmers/add/', add_farmer, name='add_farmer'),
    path('farmers/', mark_attendance, name='mark_attendance'),
    path('list/', attendance_list, name='attendance_list'),
    path('farmers/json/', farmer_list_json, name='farmer_list_json'),
]