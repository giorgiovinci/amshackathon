from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^ams/$', 'ams.views.home'),
)
