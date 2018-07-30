from django.shortcuts import render


def index(request):
    return render(request, 'nav_common.html')


def post_detail(request):
    data = {"username": "lili"}
    return render(request, "post_detail.html", context=data)

    # return HttpResponse("帖子细节页面")


def home(request):
    data = {
        "title":'论坛'
    }
    return render(request,'home.html',context=data)


def mm(request):
    return render(request,'mm.html')



def search_results(request):
    return render(request, 'search_results.html')

