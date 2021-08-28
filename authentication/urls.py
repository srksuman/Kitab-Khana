from django.urls import path
from. import views
urlpatterns = [
    path('',views.loginFunction,name="login"),
    path('register/',views.registerFunction,name="register"),
    path('reg_show/',views.signup_function,name='reg_show'),
    path('reg/',views.signup_ajax_function,name='reg'),


]
