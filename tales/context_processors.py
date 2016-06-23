from tales.models import Topic
from tales.models import Mood


def navbar(request):
    context = {'topics': Topic.objects.all(), 'moods': Mood.objects.all()}
    return context
