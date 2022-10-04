from django.urls import path
from .views import userlogin,userregister,userdashboard,extendedprofile,logout_user

app_name = 'users'

urlpatterns = [
    path('login/', userlogin, name='login'),
    path('register/', userregister, name='register'),
    path('dashboard/', userdashboard, name='dashboard'),
    path('profile/', extendedprofile, name='profile'),
    path('logout/', logout_user, name='logout'),
]