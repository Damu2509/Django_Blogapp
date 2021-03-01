from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class errors(models.Model):

    question_text = models.CharField(max_length = 1000)
    date_posted = models.DateTimeField('date posted')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.date_posted>=timezone.now()-datetime.timedelta(days=1)




class choice(models.Model):

    question = models.ForeignKey(errors , on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text