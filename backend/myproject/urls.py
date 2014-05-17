from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^ams/$',        'ams.views.home'),
    url(r'^ams/comments', 'ams.views.comments'),
    url(r'^ams/tweets',   'ams.views.tweets')
)
