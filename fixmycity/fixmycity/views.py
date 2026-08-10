from django.http import HttpResponse
from django.shortcuts import  render

def home(request):
    return render(request,"website/index.html")

def signin(request):
    return render(request,"website/signin.html")

def signup(request):
    return render(request,"website/signup.html")