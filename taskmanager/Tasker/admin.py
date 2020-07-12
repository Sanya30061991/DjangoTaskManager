from django.contrib import admin

# Register your models here.

from .models import Tasks, Users

admin.site.register(Tasks)

admin.site.register(Users)