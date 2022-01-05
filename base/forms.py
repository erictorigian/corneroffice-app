from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Client, Guest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create a client form
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = "__all__"


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        