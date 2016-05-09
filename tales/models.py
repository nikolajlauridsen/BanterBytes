from django.db import models

# Create your models here.


class Topic(models.Model):
    """The topic of an entry"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Mood(models.Model):
    """The mood of an entry"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Author(models.Model):
    """The author of an entry"""
    text = models.CharField(max_length=300)

    def __str__(self):
        """Return a string representation of the model. """
        return self.text


class Entry(models.Model):
    """Blog entry"""
    topic = models.ForeignKey(Topic)
    mood = models.ForeignKey(Mood)
    title = models.CharField(max_length=500, null=True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.title) > 50:
            return self.title[:50] + "..."
        else:
            return self.title
