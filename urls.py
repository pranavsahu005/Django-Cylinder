
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',home),
    path('home',home),
    path('save',save),
    path('display',display),
    path('remove/<int:index>',remove),
    path('remove/<int:index>',bin),
]
