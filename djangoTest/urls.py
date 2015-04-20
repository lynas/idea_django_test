from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('mysite.urls')),

    # url(r'^auth/login/$', 'mysite.views.login'),
    # url(r'^auth/logout/$', 'mysite.views.logout'),
    # url(r'^auth/invalid/$', 'mysite.views.invalid_login'),
    # url(r'^auth/authenticate/$', 'mysite.views.authenticate'),
    # url(r'^auth/loggedin/$', 'mysite.views.loggedin'),
    url(r'^auth/', include('authentication.urls')),

]

