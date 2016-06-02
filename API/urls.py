from django.conf.urls import include, url
from django.contrib import admin
import API.views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^login',API.views.login),
    url(r'^signup',API.views.signup),
    url(r'^changepassword',API.views.changepassword),
    url(r'^updateuserinfo',API.views.updateuserinfo),
    url(r'^getgames',API.views.getgames),
    url(r'^updategame',API.views.updategame),
    url(r'^creategame',API.views.creategame),
    url(r'^deletegame',API.views.deletegame),
    url(r'^createround',API.views.createround),
    url(r'^deleteround',API.views.deleteround),
    url(r'^getrounds',API.views.getrounds),
    url(r'^updateround',API.views.updateround),
    url(r'^sendmessage',API.views.sendmessage),
    url(r'^getuserinfo',API.views.getuserinfo),


]
