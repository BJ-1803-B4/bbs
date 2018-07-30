from django.conf.urls import url
from post import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post_edit$', views.post_edit, name='post_edit'),
    url(r'^post_detail/(\d+)', views.post_detail, name='post_detail'),
    url(r'^search_results/$', views.search_results, name='search_results'),


    url(r'^get_posts/', views.get_posts, name='get_posts'),
]
