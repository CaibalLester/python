from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import AilForm
from .models import Ail




# Home
def index(request):
    return render(request, "Home/index.html")



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Registration successful! You can now log in.') 
    else:
        form = RegistrationForm()
    return render(request, 'Home/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, 'Successful!')

            if user.role == 'admin':
                return redirect('/ManageApplicant')  
            elif user.role == 'applicant':
                return redirect('/DashApp')  
    else:
        form = LoginForm()

    return render(request, 'Home/login.html', {'form': form})

def delete_ail(request, ail_id):
    ail_instance = get_object_or_404(Ail, pk=ail_id)
    ail_instance.delete()
    messages.info(request, 'Entry deleted successfully!')
    return redirect('ManageApplicant') 

def DashApp(request, ail_id=None):
    if request.method == 'POST':
        if ail_id:
            # Editing an existing entry
            ail_instance = get_object_or_404(Ail, pk=ail_id)
            form = AilForm(request.POST, instance=ail_instance)
        else:
            # Creating a new entry
            form = AilForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, 'Submitted Successfully!')
    else:
        if ail_id:
            # Displaying and editing an existing entry
            ail_instance = get_object_or_404(Ail, pk=ail_id)
            form = AilForm(instance=ail_instance)
        else:
            # Displaying a blank form for creating a new entry
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

def AppView(request):
    if request.method == 'POST':
        form = AilForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Submitted Successfully!')
    else:
        form = AilForm()

    ails = Ail.objects.all()

    return render(request, 'Applicant/AppView.html', {'form': form, 'ails': ails})



def edit_ail(request, ail_id):
    ail_instance = get_object_or_404(Ail, pk=ail_id)

    if request.method == 'POST':
        form = AilForm(request.POST, instance=ail_instance)
        if form.is_valid():
            form.save()
            return redirect('ManageApplicant')  # Replace 'your_redirect_url' with the appropriate URL
    else:
        form = AilForm(instance=ail_instance)

    return render(request, 'Admin/ManageApplicant.html', {'form': form, 'ail_id': ail_id})


#Admin
def dashboard(request):
    return render(request, "Admin/dashboard.html")

def profile(request):
    return render(request, "Admin/profile.html")
def setting(request):
    return render(request, "Admin/setting.html")
def help(request):
    return render(request, "Admin/help.html")
















