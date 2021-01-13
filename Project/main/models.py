import datetime

from django.db import models
from django.utils import timezone
from django.contrib.humanize.templatetags import humanize
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    question_subtext = models.TextField(max_length=500)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(pk=1).pk)

    def get_date(self):
        return humanize.naturaltime(self.pub_date)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.comment_text

