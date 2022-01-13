from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Client, Guest, Teacher, Job
from .forms import ClientForm, EditProfileForm, GuestForm, SignUpForm, JobForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


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
            guest = form.save(commit=False)
            guest.sponsor = request.user
            guest.save()
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

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been registgered and logged in"))
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, ("You have edited your profile"))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ("You have changed your password"))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)


    context = {'form': form} 
    return render(request, 'authenticate/change_password.html', context)

@login_required
def jobsearch_home(request):
    job_count = Job.objects.all().count()
    jobs = Job.objects.all()[0:5]

    context = {'job_count': job_count, 'jobs': jobs}
    return render(request, 'jobsearch.html', context)

@login_required
def jobs(request):
    jobs = Job.objects.all()
    job_count = Job.objects.all().count()

    context = {'jobs': jobs, 'job_count': job_count}
    return render(request, 'jobs.html', context)

@login_required
def new_job(request):
    submitted = False
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid:
            job = form.save(commit=False)
            job.save()
            messages.success(request, ("Job has been saved"))
            return redirect(jobs)
    else:
        form = JobForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'submitted': submitted}
    return render(request, 'new_job.html', context)

@login_required
def job(request, job_id):
    job = Job.objects.get(pk=job_id)
    
    context = {'job': job}
    return render(request, 'job.html', context)

@login_required
def delete_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.delete()
    messages.success(request, ("Job has been deleted"))
    return redirect(jobs)
