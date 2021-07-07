from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)


def register(request):
    if request.method == "POST":

        errors = User.objects.register_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)

            return redirect('/')

        else:
            User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            date = request.POST['date'],
            password = request.POST['pass'],
            confirm_pw = request.POST['cpass'])

            messages.success(request, 'User registered!')

            return redirect('/')
    else:
        return HttpResponse('Invalid Method')

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

def welcome(request):
    return HttpResponse('Welcome to my App')

