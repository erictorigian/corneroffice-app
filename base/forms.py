from django import contrib, forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Client, Guest, Job
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#create a client form
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = "__all__"

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ('name', 'company', 'email', 'topic', 'show_date', 'source', 'comments')
    
    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)        

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['topic'].widget.attrs['class'] = 'form-control'
        self.fields['show_date'].widget.attrs['class'] = 'form-control'
        self.fields['source'].widget.attrs['class'] = 'form-control'
        self.fields['comments'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['company'].widget.attrs['placeholder'] = 'Company'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['topic'].widget.attrs['placeholder'] = 'Topics'
        self.fields['show_date'].widget.attrs['placeholder'] = 'Show Date'
        self.fields['source'].widget.attrs['placeholder'] = 'Source'
        self.fields['comments'].widget.attrs['placeholder'] = 'Comments'
        self.fields['name'].label = ''
        self.fields['company'].label = ''
        self.fields['email'].label = ''
        self.fields['topic'].label = ''
        self.fields['show_date'].label = ''
        self.fields['source'].label = ''
        self.fields['comments'].label = ''


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

class EditProfileForm(UserChangeForm):
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ""
        self.fields['username'].help_text = "<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>"
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'