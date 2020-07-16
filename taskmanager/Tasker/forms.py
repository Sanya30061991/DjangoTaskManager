from .models import Tasks
from django.forms import ModelForm, TextInput
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
