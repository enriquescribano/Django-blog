from django.db import models
from django.utils import timezone
import datetime

class User(models.Model):
    user_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.user_name

class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, blank=False)
    tags = models.ManyToManyField(Tag, blank=False)
    pub_date = models.DateTimeField('Date published')
    text = models.TextField()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    comment = models.TextField()
    pub_date = models.DateTimeField("Date")
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
        return self.comment

