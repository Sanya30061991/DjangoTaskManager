from .models import Tasks, Users
from django.forms import ModelForm, TextInput

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['login', 'password']
        widgets = {
            'login': TextInput(attrs={
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
