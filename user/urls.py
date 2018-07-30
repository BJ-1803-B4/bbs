from django.conf.urls import url
from user import views

urlpatterns = [
    url('^register/$', views.register, name='register'),
    url('^register_handler/$', views.register_handler, name='register_handler'),
    url('^login/$', views.login, name='login'),
    url('^login_handler/$', views.login_handler, name='login_handler'),
    url('^logout/$', views.logout, name='logout'),
]
