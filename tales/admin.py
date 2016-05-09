from django.contrib import admin

# Register your models here.

from tales.models import Topic, Mood, Entry, Author
admin.site.register(Topic)
admin.site.register(Mood)
admin.site.register(Author)
admin.site.register(Entry)