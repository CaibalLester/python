from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



# Home
def index(request):
    return render(request, "Home/index.html")

def login(request):
    form = LoginForm()  
    if request.method == 'POST':
        email = request.POST.get('email')  
        password = request.POST.get('password')
        role = request.POST.get('role')
        user = authenticate(request, email=email, password=password, role=role)
        if user == 'admin':
            return redirect('/dashboard')  
        else:
            form = RegistrationForm()
            messages.error(request, 'Invalid email or password. Please try again.')

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




#Admin
def dashboard(request):
    return render(request, "Admin/dashboard.html")
def ManageApplicant(request):
    return render(request, "Admin/ManageApplicant.html")
def ManageAgent(request):
    return render(request, "Admin/ManageAgent.html")
def profile(request):
    return render(request, "Admin/profile.html")
def setting(request):
    return render(request, "Admin/setting.html")
def help(request):
    return render(request, "Admin/help.html")









