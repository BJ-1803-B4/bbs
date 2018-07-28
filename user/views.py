from django.shortcuts import render


def register(request):
    return render(request,'register.html')


def register_handler(request):
    return


def login(request):
    return render(request, 'login.html')