# Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from rest_framework import viewsets

# Models, Forms, Utils, Serializers
from .models import teacher, student
from .forms import LoginForm, AddTeacherForm
from .scheduler import Scheduler
from .utils import user_login, Xlsx_extractor, OTP
from .serializers import userSerializers

# Custom
from datetime import datetime

# Token
class userviewsets(viewsets.ModelViewSet):
    queryset = user_login()
    serializer_class = userSerializers

# User
user = user_login()


# Index
def index(request):
    if user and user.authenticated:
        return redirect("home")
    else:
        return render(request, "landing_page.html")


# Login
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            global user
            user = user_login()
            user.username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user.authenticated, user.user = user.login(user.username, password)
            except:
                messages.error(request, 'Invalid username or password')
            
            if user.authenticated:
                
                if user.type == "Principle": # Principle
                    return redirect('teacher_dashboard')
                elif user.type == "Time-Table In-charge": # Time Table In charge
                    return redirect('student_dashboard')
                elif user.type == "Teacher": # Teacher
                    pass
                elif user.type == "Student": # Student
                    pass
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, "sign_in.html", {'form': form})


# Logout
def logout(request):
    global user
    user.username = None
    user.authenticated = False
    user.type = None
    user.user = None
    
    return redirect("login")


# Home
def home(request):
    return render(request, "add-teacher.html")
    if user.authenticated:
        if user.type == "Principle":
            admin_home(request)
        elif user.type == "Time-Table In-charge":
            sub_admin_home(request)
        elif user.type == "Teacher":
            teacher_home(request)
        elif user.type == "Student":
            student_home(request)
    else:
        return redirect("login")


def admin_home(request):
    if user.authenticated:
        if user.type == "Principle":
            return render(request, "")
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")


def sub_admin_home(request):
    if user.authenticated:
        if user.type == "Time-Table In-charge":
            pass
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")


def teacher_home(request):
    if user.authenticated:
        if user.type == "Teacher":
            pass
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")


def student_home(request):
    if user.authenticated:
        if user.type == "Student":
            pass
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")



def add_teacher(request):
    if user.authenticated:
        if user.type == "Principle" or user.type == "Time-Table In-charge":
            if request.method == "POST":
                form = AddTeacherForm(request.POST)
                
                if form.is_valid():
                    if form.f_name:
                        pass
                    
                    if form.file:
                        file = form.cleaned_data["file"]
                        data = Xlsx_extractor.extract_xlsx(file)
                        
                    pass
                
            return render(request, "")
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")