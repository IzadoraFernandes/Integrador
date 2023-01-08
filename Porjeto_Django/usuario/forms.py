from django.contrib.auth.models import User
from django import forms
import re

from  django  import  forms 
from  django.contrib.auth.forms  import  UserCreationForm 


class RegisterForm(forms.ModelForm):
    matricula = forms.CharField(required=True)
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        widget = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha'
            })
        }
    
    #def strong_password(password):
        #regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

        #if not regex.match(password):
            #raise ValidationError((
                #'Password must have at least onde '
            #))

