from django.conf.urls.defaults import *
from .views import complete_registration, logout


urlpatterns = patterns('',
    url(r'^complete_registration/$', complete_registration, name='users_complete_registration'),
    url(r'^logout/$', logout, name='users_logout'),
)