from django.conf.urls import patterns, include, url
from tasks.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    url(r'^task/([0-9]+)?/$', task),
    url(r'^tasks/$',tasks),
    url(r'^people/$', people),
    url(r'^profile/([0-9]+)?/$', profile),
    # url(r'^PayForward/', include('PayForward.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #develop
    url(r'^uploads/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'/home/master/djcode/payforward/uploads'}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'/home/master/djcode/payforward/media'}),
)