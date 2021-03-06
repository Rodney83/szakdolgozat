"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from views import AppRootView
from core.views import MainView

urlpatterns = [
    url(r'^$', MainView.as_view(), name="main"),
    url(r'^', include('cmdb.auth_urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/$', AppRootView.as_view(), name="root"),
    url(r'^api/core/', include('core.urls')),
    url(r'^api/inventory/', include('inventory.urls')),
    url(r'^api/changemgmt/', include('change_management.urls')),
]
