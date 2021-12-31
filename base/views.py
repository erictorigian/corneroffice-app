from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'base.html', context)


def clients(request):
    clients = {"Safran Cabin", "Connections", "Stellanis", "Other co"}

    context = {'clients': clients }
    return render(request, 'clients.html', context)

