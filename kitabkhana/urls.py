from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from kitabkhana import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about_page, name='about'),
    path('', include('authentication.urls')),
    path('', include('books.urls')),
    path('', include('chart.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
