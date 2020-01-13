from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')