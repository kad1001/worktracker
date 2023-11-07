# Python's standard datetime module
import datetime

from django.db import models
# Django's time-zone-related utility
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
# Time entry model

class TimeEntry(models.Model):
    start_time = models.DateTimeField("datetime started")
    # is_open = models.BooleanField()
    # If start_time is not null/undefined, and end_time is null/undefined, is_open should be true
    end_time = models.DateTimeField("datetime ended")
    notes = models.CharField(max_length=10000)
    def __str__(self):
        return self.notes

    