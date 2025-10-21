from django.urls import path
from .views import add_farmer, mark_attendance, attendance_list

urlpatterns = [
    path('farmers/add/', add_farmer, name='add_farmer'),
    path('farmers/', mark_attendance, name='mark_attendance'),
    path('list/', attendance_list, name='attendance_list'),
]