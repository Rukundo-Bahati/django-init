

from django import forms
from django.forms import widgets
from .models import Farmer  
class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'id': 'name',
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'id': 'phone_number',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'id': 'email',
            }),
            'password': forms.PasswordInput(attrs={
                 'class':'form-control',
                 'placeholder':"Password",
                 'id':'password'
            }),
            'farm': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Farm',
                'id': 'farm',
            }),
        }

# class AttendanceForm(forms.ModelForm):
#     class Meta:
#         model = Attendance
#         fields = '__all__'

#         widgets = {
            
#             'date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Date',
#                 'id': 'date',
#             }),
#             'farmer': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Farmer',
#                 'id': 'farmer',
#             }),
#             'is_present': forms.CheckboxInput(attrs={
#                 'class': 'form-check-input',
#                 'id': 'is_present',
#             }),
#         }
            
