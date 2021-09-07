from django.urls import path
from .views import showChart
urlpatterns = [
    path('chart/',showChart,name='chart')
]
