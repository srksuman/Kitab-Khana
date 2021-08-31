from books import views
from django.urls import path
from books import views


urlpatterns = [
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('faqs/',views.faqs, name="faqs"),
    path('products/',views.products, name="products"),
    path('services/',views.services, name="services"),
    path('single/',views.single, name="single"),
    

]