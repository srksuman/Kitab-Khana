from books import views
from django.urls import path
from books import views


urlpatterns = [
    path('contact/',views.contact, name="contact"),
    

]