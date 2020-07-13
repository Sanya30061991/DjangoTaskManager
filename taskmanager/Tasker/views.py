from django.shortcuts import render, redirect
from .models import Tasks, Users
from .forms import UsersForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def show(request):
    tasks = Tasks.objects.filter(user_id=str(0))
    return render(request, 'Tasker/tasks.html', {'tasks':tasks})

def finished(request):
    return render(request, 'Tasker/add-task.html')

def index(request):
    if request.method=="POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('login')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = UsersForm()
        context = {
        'form': form
        }
        return render(request, 'Tasker/register.html', context)