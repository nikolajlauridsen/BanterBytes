from django.shortcuts import render

from .models import Topic, Mood, Entry

# Create your views here.


def index(request):
    """The Home page of tales"""
    entries = Entry.objects.order_by("-date_added")[:4]
    topics = Topic.objects.order_by("-date_added")
    moods = Mood.objects.order_by("-date_added")
    context = {'entries':entries, 'topics':topics, 'moods':moods}
    return render(request, 'tales/index.html', context)


def topics(request):
    """Page displaying all topics"""
    topics = Topic.objects.order_by("-date_added")
    context = {'topics': topics}
    return render(request, 'tales/topics.html', context)


def moods(request):
    """Page displaying all topics"""
    moods = Mood.objects.order_by("-date_added")
    context = {'moods': moods}
    return render(request, 'tales/moods.html', context)


def topic(request, topic_id):
    """Page displaying all entries for a specific topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'tales/topic.html', context)


def mood(request, mood_id):
    """Page displaying all entries for a specific mood"""
    mood = Mood.objects.get(id=mood_id)
    entries = mood.entry_set.order_by('-date_added')
    context = {'mood': mood, 'entries': entries}
    return render(request, 'tales/mood.html', context)


def article(request, article_id):
    """Page displaying a specific article"""
    article = Entry.objects.get(id=article_id)
    topics = Topic.objects.order_by("-date_added")
    moods = Mood.objects.order_by("-date_added")
    context = {'article':article, 'topics':topics, 'moods':moods}
    return render(request, 'tales/article.html', context)


def archive(request):
    """Page displaying all blog entries"""
    entries = Entry.objects.order_by("-date_added")
    topics = Topic.objects.order_by("-date_added")
    moods = Mood.objects.order_by("-date_added")
    context = {'entries':entries, 'topics':topics, 'moods':moods}
    return render(request, 'tales/archive.html', context)


def about(request):
    """About page"""
    post_count = len(Entry.objects.all())
    context = {'p_count':post_count}
    return render(request, 'tales/about.html', context)
