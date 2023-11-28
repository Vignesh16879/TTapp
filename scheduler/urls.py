# Django
from django.urls import path, include
from rest_framework.authtoken import views

# Views
from .views import *
from .router import router


urlpatterns = [
    path("", index, name = "index"),
    path("login", login, name = "login"),
    path("accounts/", include('allauth.urls')),
    path("logout", logout, name = "logout"),
    path("home", home, name = "home"),
    path("profile", profile, name = "profile"),
    path("view", view, name="view"),
    
    path("add_holiday", add_holiday, name = "add_holiday"),    
    path("add_teacher", add_teacher, name = "add_teacher"),
    path("add_student", add_student, name = "add_student"),
    
    path("all_teacher", all_teachers, name = "all_teachers"),
    path("all_student", all_students, name = "all_students"),
    path("all_holiday",  all_holiday, name = "all_holiday"),
    
    path("edit_holiday", edit_holiday, name = "edit_holiday"),
    path("edit_student", edit_students, name = "edit_students"),
    path("edit_teacher", edit_teachers, name = "edit_teachers"),
    
    path("page_forgot_password/",page_forgot_password, name = "page_forgot_password"), 
    path("page_forgot_otp",page_forgot_otp, name = "page_forgot_otp"),
    path("page_recovery_password", page_recovery_password, name="page_recovery_password"),
    
    # APIs
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]