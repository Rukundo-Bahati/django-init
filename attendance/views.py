from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FarmerForm
from .models import Farmer


def add_farmer(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Farmer saved successfully.')
            return redirect('add_farmer')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FarmerForm()
    return render(request, 'attendance/add_farmer.html', {'form': form})


def farmer_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'attendance/farmer_list.html', {'farmers': farmers})