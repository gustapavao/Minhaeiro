from django.contrib import admin
from django.urls import path, include
import app_minhaeiro

urlpatterns = [
    path('', include('app_minhaeiro.urls')),
    path('admin/', admin.site.urls),
]
