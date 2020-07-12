from django.shortcuts import render
from .models import Tasks, Users
# Create your views here.
def show(request):
    tasks = Tasks.objects.all()
    return render(request, 'Tasker/tasks.html', {'tasks':tasks})

def finished(request):
    return render(request, 'Tasker/finished-tasks.html')

def index(request):
    return render(request, 'Tasker/register.html')