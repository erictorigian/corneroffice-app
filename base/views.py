from django.shortcuts import render
from .models import Client

def home(request):
    context = {}
    return render(request, 'base.html', context)


def clients(request):
    clients = Client.objects.all()

    context = {'clients': clients }
    return render(request, 'clients.html', context)

