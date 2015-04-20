from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^invalid/$', views.invalid_login),
    url(r'^authenticate/$', views.authenticate),
    url(r'^loggedin/$', views.loggedin),

]

