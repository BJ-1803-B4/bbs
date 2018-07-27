from django.shortcuts import render


def index(request):
    return render(request, 'nav_common.html')


def post_detail(request):
    list = ['a', 'b']
    data = {"username": list}
    return render(request, "post_detail.html", context=data)


def search_results(request):
    return render(request, 'search_results.html')
