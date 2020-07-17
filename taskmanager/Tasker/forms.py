from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User

class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'type':"email",
                 'id':"inputEmail",
                  'class':"form-control",
                   'placeholder':"Email address",
                    'required':"",
                     'autofocus':"",
            }),
            'password' :TextInput(attrs={
                'type':"password",
                 'id':"inputPassword",
                  'class':"form-control",
                   'placeholder':"Password",
                    'required':""
            })
        }



class TaskForm(ModelForm):
    class Meta: 
        model = Tasks
        fields = ['title', 'desc']
        widgets = {
            'title': TextInput(attrs={
                'type':"text",
                'class':"form-control",
                'id':"formGroupExampleInput",
                'placeholder':"Task's title",
            }),
            'desc':Textarea(attrs={
                'type':"textarea",
                'class':"form-control",
                'id':"formGroupExampleInput2",
                'placeholder':"Description of the task",
            })
        }