from django.shortcuts import render


def index(request):
    
    return render(request, 'nav_common.html')