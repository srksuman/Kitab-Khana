from django.urls import path
from. import views
urlpatterns = [
    path('',views.loginFunction,name="login"),
    path('register/',views.registerFunction,name="register")

]
