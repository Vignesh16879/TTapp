from django.urls import include, path
from . import views


urlpatterns = [
    # Authentication Token
    
    # Login
    path('', views.login, name = 'login'),
    
    # Home Page(Admin / Teacher)
    path('home', views.index, name = 'home'),
]