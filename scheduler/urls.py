# Django
from django.urls import path, include
from rest_framework.authtoken import views

# Views
from .views import index, login, logout, home
from .router import router


urlpatterns = [
    path("", index, name = "index"),
    path("login", login, name = "login"),
    path("accounts/", include('allauth.urls')),
    path("logout", logout, name = "logout"),
    path("home", home, name = "home"),
    
    # APIs
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]