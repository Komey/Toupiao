from django.conf.urls import include, url
from django.contrib import admin
import hello.views
import API.urls
urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello.views.index, name='index'),
    url(r'^api/', include(API.urls)),
]
