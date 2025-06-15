from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse, render

def home(request):
    return render(request, "home.html")

def save(request):
    radius =int (request.GET.get('radius'))
    height =int (request.GET.get('height'))
    pi=3.14159
    volume=pi*(radius*radius)*height
    data = {'radius': radius, 'height':height, 'volume': volume}
    return render(request, "display.html", data)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('save/', save),
]