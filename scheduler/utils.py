# Django
from django.conf import settings
from django.http import JsonResponse
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models import Q

# Models, Forms
from .models import teacher, student

# Others
import os
import random
import string
import shutil
import hashlib
from twilio.rest import Client
from datetime import datetime, timedelta


# Login
class user_login():
    username = ""
    authenticated = bool
    user = teacher()
    
    def login(self, username, password):
        
        try:
            result = teacher.objects.filter((Q(username = username) | Q(email = username) | Q(phone = username)) & Q(password = hashlib.sha256().update(password.encode()).hexdigest()))
        except:
            result = student.objects.filter((Q(username = username) | Q(email = username) | Q(phone = username)) & Q(password = hashlib.sha256().update(password.encode()).hexdigest()))
        
        if result.exists():
            self.authenticated = True
            self.user = result.first()
            
            return self.authenticated, self.user
        else:
            return False, None


# Xlsx extractor
class Xlsx_extractor():
    def get_file_extension(file_path):
        try:
            _, file_extension = os.path.splitext(file_path)
            return file_extension.lower() 
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
        
    def file_upload(self, file):
        current_time = timezone.now().strftime("%Y%m%d%H%M%S")
        type = self.get_file_extension(file)
        new_name = "teacher_details_{current_time}" + type
        
        try:
            os.rename(file, new_name)
            print(f"File renamed successfully to {new_name}")
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission error. Make sure you have the necessary permissions.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        try:
            shutil.move(file, "Teachers/")
            print(f"File moved successfully to {'Teachers/'}")
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission error. Make sure you have the necessary permissions.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return "Teachers/", new_name, current_time
    
    
    def extract_xlsx(self, file):
        base_dir, filename, current_time = self.file_upload(file)


# OTP
class OTP():
    valid_till = datetime.now()
    otp = ""
    
    def generate_otp(self, length = 6):
        self.valid_till = datetime.now() + timedelta(minutes = 5)
        characters = string.digits
        self.otp = ''.join(random.choice(characters) for _ in range(length))
        
        return self.valid_till, self.otp


    def send_otp_phone(phone_number, otp):
        account_sid = "ACd5a3b4236c548582b3079c4e4a8219b7"
        auth_token = "f7126fb59f26189bd21888869886c972"
        twilio_phone_number = "+12512399796"

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = f'Your OTP is: {otp}',
            from_ = twilio_phone_number,
            to = phone_number
        )


    def send_otp_via_email(request, email, otp):
        subject = 'OTP'
        message = f'Your OTP is: {otp}'
        from_email = 'vignesh20152@iiitd.ac.in'
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return JsonResponse({'message': 'OTP sent successfully'})
        except Exception as e:
            return JsonResponse({'message': f'Failed to send OTP: {str(e)}'}, status=500)
    
    
    def verify_otp(self, otp):
        if datetime.now() <= self.valid_till:
            if otp == self.otp:
                return True, "Successful"
            else:
                return False, "Invalid OTP"
        else:
            return False, "OTP, time out. Try again"
    
    
    def verify_phone(self, otp):
        pass