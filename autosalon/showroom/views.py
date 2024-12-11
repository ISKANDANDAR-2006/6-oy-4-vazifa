from django.shortcuts import render
from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'showroom/home.html', {'brands': brands, 'cars': cars})
