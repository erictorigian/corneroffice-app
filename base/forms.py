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
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}))
    first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)        
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['Placeholder'] = 'Re-enter your password'
        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        self.fields['username'].help_text = "<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"
        self.fields['password1'].help_text = "<small>Your password must contain at least 8 character, cannot be a common password or all numbers</small>"
        self.fields['password2'].help_text = "<small>Enter the same password as before, for verification.</small>"
       