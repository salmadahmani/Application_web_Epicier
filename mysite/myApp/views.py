
import form as form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ClientsForm, CreateUserForm, CreditsForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages
from.models import Produits, Clients, Credits
from django.contrib.auth import logout

# def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())


def Home(request):
    return render(request, 'Home.html',)

def Login(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                return redirect('home')
            if form is not None:
                messages.info(request, "Invalid username or password.")
        context = {}
        return render(request, 'log in.html', context)


def Registration (request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registre.html', context)

def Logout (request):
    logout(request)
    return redirect('log in')

def clients(request):

    form = ClientsForm()
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form, 'clients': Clients.objects.all()}

    return render(request, 'clients.html', context, )

def produits(request):
    produits = Produits.objects.all()
    return render(request, 'produit.html', {'produits': produits})

def credits(request):
    form = CreditsForm()
    if request.method == "POST":
        form = CreditsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form, 'credits': Credits.objects.all()}
    return render(request, 'credits.html', context)










