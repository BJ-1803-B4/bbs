from django.core import signing
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from user.forms import RegisterForm, LoginForm
from user.models import User


def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form':form})


def register_handler(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create(form.cleaned_data.get('username'), form.cleaned_data.get('password'))
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    raise Http404


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form':form})


def login_handler(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['username'] = username
            response = HttpResponseRedirect(reverse('index'))
            response.set_cookie('uid', cookie_handler(username))
            return response
        else:
            return render(request, 'login.html', {'form': form})
    raise Http404


def cookie_handler(username):
    timestamp_signing = signing.TimestampSigner()
    value1 = signing.dumps({"username": username})
    value2 = timestamp_signing.sign(value1)
    return value2
