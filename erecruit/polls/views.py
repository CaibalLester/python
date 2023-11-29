from django.http import HttpResponse
from django.shortcuts import render

# Home
def index(request):
    return render(request, "Home/index.html")
def login(request):
    return render(request, "Home/login.html")
def register(request):
    return render(request, "Home/register.html")


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

