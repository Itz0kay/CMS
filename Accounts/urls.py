from django.urls import path
from Accounts.views import *

urlpatterns = [
    path('register',register, name='register'),
    path('login',login, name='login'),
    path('logout',logout, name='logout'),
]