from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth import views

template_name = {'template_name': 'core/login.html'}

app_name = 'rest_framework'
urlpatterns = [
    url(r'^login/$', views.login, template_name, name='login'),
    url(r'^logout/$', views.logout, template_name, name='logout'),
]