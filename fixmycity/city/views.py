from django.shortcuts import render

# Create your views here.
def all_city(request):
    return render(request,'city/all_city.html')