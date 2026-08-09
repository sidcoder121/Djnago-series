from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World,You are siddharth saxena")

def about(request):
    return HttpResponse("This is my About page")