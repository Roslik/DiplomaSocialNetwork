from django.conf.urls import patterns, url

from news.views import NewsListView, NewsDetailView 

urlpatterns = patterns('',
url(r'^$', NewsListView.as_view(), name='list'),
url(r'^(?P<pk>\d+)/$', NewsDetailView.as_view()),
)
