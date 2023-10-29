# Django
from django.shortcuts import render, redirect
from django.contrib import messages

# Models, Forms
from .models import user_login, teacher
from .forms import LoginForm

# Custom
from .scheduler import Scheduler


# Login
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user = user_login()
            user.username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user.authenticated, user.teacher = user.login(user.username, password)
            except teacher.DoesNotExist:
                    messages.error(request, 'Invalid username or password')
            
            if user.authenticated:
                if user.type == "Principle": # Principle
                    return redirect('teacher_dashboard')
                elif user.type == "Time-Table In-charge": # Time Table In charge
                    return redirect('student_dashboard')
                elif user.type == "Teacher": # Teacher
                    pass
                else: # Student
                    pass
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, "sign-in.html", {'form': form})


# Logout
def logout(request):
    return redirect(request, "login")


# Home
def home(request):
    return redirect(request, "login")


def admin_home(request):
    pass


def teacher_home(request):
    pass