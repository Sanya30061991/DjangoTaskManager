from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, UserManager
from .models import Tasks
from .forms import UsersForm, TaskForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def show(request):
    tasks = Tasks.objects.filter(user_id=str(request.user.id))
    return render(request, 'Tasker/tasks.html', {'tasks':tasks, 'id':request.user.id})


def finished(request):
    form = TaskForm()
    context = {
        'form':form,
        'errors': []
    }
    if request.method == "POST":
        deect = request.POST.copy()
        di1 = {'user_id':request.user.id}
        deect.update(di1)
        form = TaskForm(deect)
        form.save()
        return redirect('main')
    else:
        context['errors'].append("Method = GET")
        return render(request, 'Tasker/add-task.html', context)


def glue(request):
    form = UsersForm()
    context = {
            'form': form,
            'errors': []
        }
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if user is not None and password==user.password and username==user.username:
            login(request, user)
            return redirect('main')
        elif user is not None or user!=user.password:
            context['errors'].append("Invalid login or password.")
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