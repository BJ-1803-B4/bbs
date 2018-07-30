from django.core import signing
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.serializers import serialize

from post.forms import PostEditForm
from post.models import Post
from user.models import User


# 登录认证装饰器
def login_required(view_fun):
    def valid_cookie_and_session(request):
        try:
            username_cookie = request.COOKIES.get('uid')
            username_session = request.session.get('username')
            timestamp_signing = signing.TimestampSigner()
            result = timestamp_signing.unsign(username_cookie, max_age=60*60*24)
            username = signing.loads(result)['username']
            if username and username_session == username:
                return view_fun(request)
            else:
                return redirect('login')
        except:
            return redirect('login')
    return valid_cookie_and_session


# 将经过加密的uid解密为username
def get_username(request):
    uid = request.COOKIES.get('uid', 0)
    if not uid:
        return uid
    timestamp_signing = signing.TimestampSigner()
    result = timestamp_signing.unsign(uid, max_age=60 * 60 * 24)
    username = signing.loads(result)['username']
    return username


def index(request):
    username = get_username(request)
    posts = Post.objects.all().order_by('-timestamp')[:20]
    return render(request, 'index.html', {'username': username, 'posts': posts})


# 登录以后才可以发表帖子
@login_required
def post_edit(request):
    form = PostEditForm()
    username = get_username(request)
    if request.method == 'POST':
        form = PostEditForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=username)[0]
            title = form.cleaned_data['post_title']
            cont_str = form.cleaned_data['post_content']
            cont_html = cont_str
            post = Post.objects.create(user=user, author=username, title=title, cont_str=cont_str, cont_html=cont_html)
            return redirect(reverse('post_detail', args=(post.id,)))
    return render(request, 'post_edit.html', {'form': form, 'username': username})


def post_detail(request, pid):
    post = get_object_or_404(Post, pk=pid)
    username = get_username(request)
    return render(request, "post_detail.html", {'post': post, 'username': username})


def search_results(request):
    username = get_username(request)
    return render(request, 'search_results.html', {'username': username})


# js异步获取帖子列表
def get_posts(request):
    if request.method == 'GET':
        offset = int(request.GET.get('offset'))
        start = int(request.GET.get('start'))
        queryset = Post.objects.order_by('-timestamp').filter(pk__in=range(start, start + offset))
        posts = serialize('json', queryset)     # 将查询集序列化成json
        response = JsonResponse({'data': posts})
        return response
    raise Http404
