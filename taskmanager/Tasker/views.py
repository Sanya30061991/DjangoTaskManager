from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, UserManager
from .models import Tasks
from .forms import UsersForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def show(request):
    tasks = Tasks.objects.filter(user_id=str( ))
    return render(request, 'Tasker/tasks.html', {'tasks':tasks})


def finished(request):
    return render(request, 'Tasker/add-task.html')


def glue(request):
    form = UsersForm()
    context = {
            'form': form,
            'errors': []
        }
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('main')   
        # else:
        context['errors'].append(user)
        return render(request, 'Tasker/login.html', context)
    else:
        return render(request, 'Tasker/login.html', context)



def index(request):
    context = {
            'form': UsersForm(),
            'errors': []
        }
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username = username)
        if len(user)!=0:
            context['errors'].append("User with this login already has been registered.")
            return render(request, 'Tasker/register.html', context)
        else:
            form = UsersForm(request.POST)
            form.save()
            return redirect('loogg')
        
    else:
        return render(request, 'Tasker/register.html', context)