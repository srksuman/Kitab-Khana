from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def function(request):
    return render(request,"html/base.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',function)
]
