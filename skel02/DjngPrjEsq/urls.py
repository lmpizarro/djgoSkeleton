"""DjngPrjEsq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
#from rest30lines.views import FileViewSet
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from quickstart import views

from django.contrib import admin

import catalog

router = DefaultRouter()
#router.register(r'rest30lines', FileViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^accounts/profile/', admin.site.urls),
    #url(r'', include('myApp01.urls')),
    #url(r'^rest30lines/', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^', include('catalog.urls')),
    #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
