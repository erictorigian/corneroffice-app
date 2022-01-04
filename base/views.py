from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Client, Guest
from .forms import ClientForm, GuestForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    client_count = Client.objects.all().count()
    guest_count = Guest.objects.all().count() 
    context = {'guest_count': guest_count, 'client_count': client_count}
    return render(request, 'home.html', context)

@login_required
def clients(request):
    clients = Client.objects.all()

    context = {'clients': clients}
    return render(request, 'clients.html', context)

@login_required
def client(request, client_id):
    client = Client.objects.get(pk=client_id)

    context = {'client': client}
    return render(request, 'client.html', context)

@login_required
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

@login_required
def delete_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    client.delete()
    messages.success(request, ("Client has been deleted"))
    return redirect(clients)

@login_required
def update_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('clients')
    context = {'client': client, 'form': form}
    return render(request, 'update_client.html', context)

# Guests

@login_required
def guests(request):
    guests = Guest.objects.all()
    guest_count = Guest.objects.all().count() 
    context = {'guests': guests, 'guest_count': guest_count}
    return render(request, 'guests.html', context)

@login_required
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

@login_required
def guest(request, guest_id):
    guest = Guest.objects.get(pk=guest_id)
    
    context = {'guest': guest}
    return render(request, 'guest.html', context)

@login_required
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

#Authetication
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('home')
        else:
            messages.error(request, ("Error logging into the system"))
            return redirect('login')
    else:
        context = {}
        return render(request, 'authenticate/login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')
