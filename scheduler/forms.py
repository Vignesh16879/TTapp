# Django
from django import forms
from django.contrib.postgres.fields import ArrayField


# Login
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput)
    

# Add Teacher File
class AddTeacherForm(forms.Form):
    f_name = forms.CharField(max_length = 25)
    l_name = forms.CharField(max_length = 25)
    email = forms.CharField(max_length = 30)
    join_date = forms.DateField()
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    phone = forms.CharField(max_length = 10)
    gender =  forms.CharField(max_length = 7)
    post = forms.CharField(max_length = 25)
    dob = forms.DateField()
    subjects = ArrayField(forms.CharField(max_length = 25))
    edu = forms.Textarea()
    file = forms.FileField()


# Add Student File 
class AddStudentForm(forms.Form):
    f_name = forms.CharField(max_length = 25)
    l_name = forms.CharField(max_length = 25)
    email = forms.CharField(max_length = 30)
    join_date = forms.DateField()
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    phone = forms.CharField(max_length = 10)
    gender =  forms.CharField(max_length = 7)
    post = forms.CharField(max_length = 25)
    dob = forms.DateField()
    file = forms.FileField()