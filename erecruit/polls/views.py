from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import AilForm
from .models import Ail


# Home
def index(request):
    return render(request, "Home/index.html")



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')  # Replace 'home' with the name of your home page URL
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()

    return render(request, 'Home/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Registration successful! You can now log in.') 
    else:
        form = RegistrationForm()
    return render(request, 'Home/register.html', {'form': form})


def DashApp(request):
    if request.method == 'POST':
        form = AilForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Submitted Successfully!')
    else:
        form = AilForm()

    ails = Ail.objects.all()

    return render(request, 'Applicant/DashApp.html', {'form': form, 'ails': ails})

def ManageApplicant(request):
    if request.method == 'POST':
        form = AilForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Submitted Successfully!')
    else:
        form = AilForm()

    ails = Ail.objects.all()

    return render(request, 'Admin/ManageApplicant.html', {'form': form, 'ails': ails})
   


#Admin
def dashboard(request):
    return render(request, "Admin/dashboard.html")

def profile(request):
    return render(request, "Admin/profile.html")
def setting(request):
    return render(request, "Admin/setting.html")
def help(request):
    return render(request, "Admin/help.html")

















