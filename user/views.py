from django.shortcuts import render

from user.forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form':form})


def register_handler(request):
    return


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form':form})


def login_handler(request):
    return None