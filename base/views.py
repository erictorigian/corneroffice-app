from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Client, Guest
from .forms import ClientForm, GuestForm


def home(request):
    context = {}
    return render(request, 'base.html', context)


def clients(request):
    clients = Client.objects.all()

    context = {'clients': clients}
    return render(request, 'clients.html', context)


def client(request, client_id):
    client = Client.objects.get(pk=client_id)

    context = {'client': client}
    return render(request, 'client.html', context)


def new_client(request):
    submitted = False
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, ("Client has been saved"))
            return redirect(clients)
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted = True
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

# Guests


def guests(request):
    guests = Guest.objects.all()
    guest_count = Guest.objects.all().count() 
    context = {'guests': guests, 'guest_count': guest_count}
    return render(request, 'guests.html', context)


def new_guest(request):
    submitted = False
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, ("Client has been saved"))
            return redirect(clients)
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'new_guest.html', context)


def guest(request, guest_id):
    guest = Guest.objects.get(pk=guest_id)
    
    context = {'guest': guest}
    return render(request, 'guest.html', context)

def new_guest(request):
    submitted = False
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, ("Guest has been saved"))
            return redirect(guests)
    else:
        form = GuestForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'new_guest.html', context)