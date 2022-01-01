from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Client

#create a client form
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"