from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.index),
    path('tasks',views.show),
    path('finished-tasks', views.finished)
]
