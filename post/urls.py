from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^home/', views.home, name='home'),

    url(r'^post_detail/$', views.post_detail, name='post_detail'),
    url(r'^search_results/$', views.search_results, name='search_results'),

]
