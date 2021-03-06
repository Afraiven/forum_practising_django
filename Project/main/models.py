import datetime

from django.db import models
from django.utils import timezone
from django.contrib.humanize.templatetags import humanize
from django.contrib.auth.models import User


class Report(models.Model):
    blinking = models.CharField(max_length=150)
    distance = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(pk=1).pk)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_date(self):
        return humanize.naturaltime(self.pub_date)

    def __str__(self):
        return self.user.username


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    question_subtext = models.TextField(max_length=500)
    pub_date = models.DateTimeField('date published')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(pk=1).pk)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def get_date(self):
        return humanize.naturaltime(self.pub_date)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Category(models.Model):
    name = models.CharField(max_length=30)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


def return_date_time():
    now = timezone.now()
    return now + timezone.timedelta(days=1)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    pub_date = models.DateTimeField('date published', default=return_date_time)
    comment_text = models.CharField(max_length=400)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(pk=1).pk)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_date(self):
        return humanize.naturaltime(self.pub_date)

    def __str__(self):
        return self.comment_text


class VoterUp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class VoterDown(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

