from books import views
from django.urls import path


urlpatterns = [
    path('', views.index_page, name="home"),
    path('contact/', views.contact, name="contact"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('add/', views.add, name="add"),
    path('view/', views.view, name="view"),
    path('delete/<int:id>/', views.delete_book, name="deletebook"),
    path('update/<int:id>/', views.update_book, name="updatebook"),
    path('about/', views.about_page, name="about"),
    path('products/', views.product_page, name="products"),
    path('singlepage/', views.single_page_detail, name='single'),
    path('singlepage/<int:id>/', views.single_page_detail, name='single')
]
