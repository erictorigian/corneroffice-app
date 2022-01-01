from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Client
from .forms import ClientForm

def home(request):
    context = {}
    return render(request, 'base.html', context)


def clients(request):
    clients = Client.objects.all()

    context = {'clients': clients }
    return render(request, 'clients.html', context)

def client(request, client_id):
    client = Client.objects.get(pk=client_id)


    context = {'client': client} 
    return render(request, 'client.html', context)

def new_client(request):
    submitted=False
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, ("Client has been saved"))
            return redirect(clients)
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted=True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'new_client.html', context)

def delete_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    client.delete()
    messages.success(request, ("Client has been deleted"))
    return redirect(clients)

def update_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('clients')
    context = {'client': client, 'form': form}
    return render(request, 'update_client.html', context)
