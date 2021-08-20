from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('registerfrontend.urls')),
    path('',include('authentication.urls')),
    path('',include('books.urls')),
    path('',include('chart.urls')),

]
