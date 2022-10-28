from django.contrib import admin
from django.urls import path

from blog.views import home

urlpatterns = [
    path('administrador/', admin.site.urls),
    path('', home),
]
