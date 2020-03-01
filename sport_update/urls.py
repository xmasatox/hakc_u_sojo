from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooter, name='index'),
    path('admin/', admin.site.urls),
]