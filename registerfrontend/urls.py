from registerfrontend import views
from django.urls import path

urlpatterns = [
    path('regis', views.registerfrontend, name="registerfrontend"),

]