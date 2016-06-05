"""Defines patterns for tales"""

from django.conf.urls import url
from . import views

app_name = 'tales'
urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),
    # Show all entries for a specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Show all moods
    url(r'^moods/$', views.moods, name='moods'),
    # Show all etries for a specific mood
    url(r'^moods/(?P<mood_id>\d+)/$', views.mood, name='mood'),
    # display a specific article
    url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
    # archive. Display all blog entries
    url(r'^archive/$', views.archive, name='archive'),
    # About page
    url(r'^about/$', views.about, name='about')
]
