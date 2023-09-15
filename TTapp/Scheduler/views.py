import pandas as pd
import glob as glob
import os
import uuid

# Django 
from django.shortcuts import redirect, render
from django.db import IntegrityError

#
from . import models
from . import forms


# Create your views here.
def login(request):
    return render(request, "login.html")


def register_user(request):
    pass


def index(request):
    if True:
        if True:
            return render(request, "admin_index.html")
        else:
            return render(request, "teacher_index.html")
    else:
        return redirect(request, 'login')


def logout(request):
    pass

    return redirect(request, 'login')


def get_next_teacher_details_number():
    max_number = models.UploadedFile.objects.filter(renamed_filename__startswith='teacher_details_').aggregate(
        models.Max(models.Cast(models.Substr('renamed_filename', 15), models.IntegerField()))
    )['renamed_filename__max']

    if max_number is None:
        return "000"
    else:
        next_number = max_number + 1
        
        return f"{next_number:03d}"


def upload_file(request):
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            uploaded_file = request.FILES['file']
            original_filename = uploaded_file.name
            unique_number = get_next_teacher_details_number()
            unique_filename = f"teacher_details_{unique_number}.xlsx"
            path_to_save = os.path.join('uploads', unique_filename)
            
            with open(path_to_save, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            models.UploadedFile.objects.create(
                original_filename = original_filename,
                renamed_filename = unique_filename
            )
            
            return redirect('success')
    else:
        form = forms.UploadFileForm()
    
    return render(request, 'upload.html', {'form' : form})


def xlsx_to_db(file_name):
    base_dir = "Uploads/"
    file_dir = base_dir / file_name
    
    try:
        file = pd.read_excel(file_dir)
        
        for index, row in file.iterrows():
            try:
                models.teacher.objects.create(
                    id = row["Teacher Id"],
                    name = row["First Name"] + " " + row["Last Name"],
                    email = row["Email"],
                    subject = row["Subject"].split(","),
                    post = row["Post"],
                    classes = [],
                )
            except IntegrityError:
                pass # Handle duplicate entries
    except Exception as e:
        print(f'Error importing data: {str(e)}')
        
        return False
    
    try:
        models.teacher.save()
    except Exception as e:
        print(f'Error saving data: {str(e)}')
        
        return False
    
    return True


def scheduler():
    pass