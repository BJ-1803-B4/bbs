from django.conf.urls import url
from user import views

urlpatterns = [
    url('^register/$', views.register, name='register'),
    url('^login/$', views.login, name='login'),
]
