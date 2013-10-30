from django.conf.urls import patterns, include, url
# from djcelery.tests.test_snapshot import create_task
from tasks.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^task/([0-9]+)?/$', task),
    url(r'^tasks/$',tasks),
    url(r'^people/$', people),
    url(r'^create_task/$', create_task),
    url(r'^profile/([0-9]+)?/$', profile),

    #loginza
    (r'^loginza/', include('loginza.urls')),
    url(r'^users/', include('users.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #develop
    url(r'^uploads/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'/home/master/djcode/payforward/uploads'}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'/home/master/djcode/payforward/media'}),
)