from books import views
from django.urls import path


urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('add/', views.add, name="add"),
    path('view/', views.view, name="view"),
    path('delete/<int:id>/', views.delete_book, name="deletebook"),
    path('update/<int:id>/', views.update_book, name="updatebook")
]
