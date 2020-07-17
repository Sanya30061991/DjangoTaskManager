from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.index, name='reg'),
    path('tasks',views.show, name = 'main'),
    path('add-task', views.finished, name = 'create'),
    path('login', views.glue, name="loogg"),
    path('logout-exec', views.loggone, name="col")
]
