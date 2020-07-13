from django.shortcuts import render, redirect, HttpResponse
from .models import Tasks, Users
from .forms import UsersForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def show(request):
    tasks = Tasks.objects.filter(user_id=str( ))
    return render(request, 'Tasker/tasks.html', {'tasks':tasks})


def finished(request):
    return render(request, 'Tasker/add-task.html')


def index(request):
    if request.method=="POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            uss = len(list(Users.objects.values()))
            username = form.cleaned_data.get('login')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            render(request,)
            return 
    else:
        form = UsersForm()
        context = {
        'form': form
        }
        return render(request, 'Tasker/register.html', context)