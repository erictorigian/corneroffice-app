from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Client, Guest

#create a client form
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = "__all__"