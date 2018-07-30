from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post_detail/', views.post_detail, name='post_detail'),
    url(r'^home/', views.home, name='home'),

]
