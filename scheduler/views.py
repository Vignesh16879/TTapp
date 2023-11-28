# Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from rest_framework import viewsets

# Models, Forms, Utils, Serializers
from .models import teacher, student, timetable
from .forms import *
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
theme = "dark"

# Index
def index(request):
    if user and user.authenticated:
        return redirect("home")
    else:
        return render(
            request, 
            "landing_page.html",
            {
                "theme" : theme
            }            
        )


# Login
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user = user_login()
            
            user.username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user.authenticated, user.user = user.login(user.username, password)
            except:
                messages.error(request, 'Invalid username or password')
            
            if user and user.authenticated:
                
                if user.type == "Principle": # Principle
                    return redirect('teacher_dashboard')
                elif user.type == "Time-Table In-charge": # Time Table In charge
                    return redirect('student_dashboard')
                elif user.type == "Teacher": # Teacher
                    pass
                elif user.type == "Student": # Student
                    return redirect('student_dashboard')
                return redirect("home")
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(
        request, 
        "sign_in.html", 
        {
            "theme" : theme,
            "form" : form
        }
    )

user_otp = OTP()
otp_send = False
otp_verified = False
email = ""
#
def page_forgot_password(request):
    global user_otp
    global otp_send
    global email
    error = None
    
    if request.method == "POST":
        form = ForgotPasswordEmailForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data["email"]
            print("Check for user's email")
            check = user.if_user_exits(email)
            
            if check:
                if email and not otp_send:
                    print(f"Sending OTP to {email}")
                    user_otp.valid_till, user_otp.otp = user_otp.generate_otp()
                    otp_send = user_otp.send_otp_via_email(email, user_otp.otp)
                    
                    if otp_send:
                        return redirect("page_forgot_otp")
            else:
                print(f"User's email: {email} doesn't exits.")
                error = f"User's email: {email} doesn't exits."
    else:
        form = ForgotPasswordEmailForm()
    
    return render(
        request,
        "page-forgot-password.html",
        {
            "theme" : theme,
            "form" : form,
            "error" : error,
        }
    )


def page_forgot_otp(request):
    global user_otp
    global otp_send
    global otp_verified
    
    if otp_send and not otp_verified:
        if request.method == "POST":
            form = ForgotPasswordOTPForm(request.POST)
            
            if form.is_valid():
                otp = form.cleaned_data["otp"]
                print("Verify OTP")
                verify_otp, error_message = user_otp.verify_otp(otp)
                
                if verify_otp:
                    otp_verified = True
                    print("OTP verified")
                    return redirect("page_recovery_password")
                else:
                    print("OTP unverified")
                    messages.error(request, error_message)
                    return redirect("page_forgot_otp")
        else:
            form = ForgotPasswordOTPForm()
    else:
        return redirect("page_forgot_password")
    
    return render(
        request,
        "page-forgot-otp.html",
        {
            "theme" : theme,
            "form" : form,
        }
    )


def page_recovery_password(request):
    global otp_send
    global otp_verified
    global email
    temp = email
    
    if otp_send and otp_verified:
        if request.method == "POST":
            otp_send = False
            otp_verified = False
            email = None
            form = RecoverPasswordForm(request.POST)
            print(form)
            if form.is_valid:
                print("changing password")
                
                pwd = form.cleaned_data["password"]
                confirm_pwd = form.cleaned_data["confirm_password"]
                
                if pwd == confirm_pwd:
                    pas = user_login.change_user_password(temp, pwd)
                    
                    if pas:
                        return redirect("login")
                    else:
                        print("Couldn't change")
                else:
                    print("no")
        else:
            form = RecoverPasswordForm()
    else:
        return redirect("page_forgot_password")
    
    return render(
        request,
        "page-recover.html",
        {
            "theme" : theme,
            "form" : form,
        }
    )

# Logout
def logout(request):
    global user
    user.username = None
    user.authenticated = False
    user.type = None
    user.user = None
    
    return redirect("login")


# Profile
def profile(request):
    if user and user.authenticated:
        if user.type == "Student":
            pass
        else:
            return render(
                request, 
                "app-profile.html", 
                {
                    "theme" : theme,
                    "username"      : user.user.f_name + user.user.l_name,
                    "email"         : user.user.email,
                    "availability"  : user.user.post,
                }
            )
    else:
        return redirect("login")


# Home
def home(request):
    
    if user and user.authenticated:
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
    if user and user.authenticated:
        if user.type == "Principle":
            return render(
                request, 
                "time_table.html",
                {
                    "theme" : theme,
                }
            )
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")


def sub_admin_home(request):
    if user and user.authenticated:
        if user.type == "Time-Table In-charge":
            return render(
                request, 
                "time_table_1.html",
                {
                    "theme" : theme,
                }
            )
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")


def teacher_home(request):
    if user and user.authenticated:
        if user.type == "Teacher":
            pass
        else:               
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")


def student_home(request):
    if user and user.authenticated:
        if user.type == "Student":
            pass
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")



def add_teacher(request):
    return render(request, "add-teacher.html", {"theme" : theme})
    if user and user.authenticated:
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
                
            return render(
                request, 
                "",
                {
                    "theme" : theme,
                }
            )
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")


def add_student(request):
    return render(request, "add-student.html", {"theme" : theme})
    if user and user.authenticated:
        if user.type == "Principle" or user.type == "Time-Table In-charge":
            if request.method == "POST":
                form = AddStudentForm(request.POST)
                
                if form.is_valid():
                    if form.f_name:
                        pass
                    
                    if form.file:
                        file = form.cleaned_data["file"]
                        data = Xlsx_extractor.extract_xlsx(file)
                        
                    pass
                
            return render(
                request, 
                "",
                {
                    "theme" : theme,
                }
            )
        else:
            messages.error(request, "You are not Authorized to view this page")
    else:
        return redirect("login")


def view(request):    
    # xx = Scheduler(6, 6, 3)
    # teachers_details = xx.fetch_teacher_details_from_xlsx()
    data = timetable[0]["Time Table"]
    istable = str(timetable[0]["Class"]) + "-" + timetable[0]["Section"]
    isteacher = False
    
    if request.method == "POST":
        form = TimeTableForm(request.POST)
        
        if form.is_valid():
            cal = form.cleaned_data["class"]
            sec = form.cleaned_data["section"]
            data = []
            
            print("Searching classes")
            
            for i in range(0, len(timetable)):
                if timetable[i]["Class"] == cal and timetable[i]["Section"]:
                    print("class found")
                    data = timetable[i]["Time Table"]
                    istable = str(cal) + "-" + sec
            
            # teach = form.cleaned_data["teacher"]
            
            # for yy in teachers_details:
            #     if teach in xx["Name"] or teach == xx["Id"]:
            #         print("teacher found")
            #         data = yy["Time Table"]
            #         isteacher = xx["Name"]
    else:
        form = TimeTableForm()
    
    return render(
        request,
        "time_table.html",
        {
            "c" : 0,
            "temp" : [0,1,2,3,4,5,6],
            "istable" : istable,
            "isteacher" : isteacher,
            "message" : "No data available to view",
            "day" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "timetable" : data
        }
    )


def view_teacher(request):
    if user and user.authenticated:
        pass
    else:
        return redirect("login")


def view_student(request):
    if user and user.authenticated:
        pass
    else:
        return redirect("login")


def view_time_table(request):
    if user and user.authenticated:
        pass
    else:
        return redirect("login")


def add_or_update_grade(request):
    if user and user.authenticated:
        pass
    else:
        return redirect("login")


def view_grades(request):
    if user and user.authenticated:
        pass
    else:
        return redirect("login")
    

def all_teachers(request):
    return render(request, "all-teachers.html", {"theme" : theme})

def all_students(request):
    return render(request, "all-students.html", {"theme" : theme})

def all_holiday(request):
    return render(request, "all-holiday.html", {"theme" : theme})

def add_holiday(request):
    return render(request, "add-holiday.html", {"theme" : theme})

def edit_teachers(request):
    return render(request, "edit-teacher.html", {"theme" : theme})

def edit_students(request):
    return render(request, "edit-student.html", {"theme" : theme})

def edit_holiday(request):
    return render(request, "edit-holiday.html", {"theme" : theme})