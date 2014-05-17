from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^ams/$',        'ams.views.venues'),
    url(r'^ams/comments', 'ams.views.comments'),
    url(r'^ams/photos', 'ams.views.photos'),
    url(r'^ams/tweets',   'ams.views.tweets')
)
