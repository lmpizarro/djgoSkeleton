import datetime
from django.utils import timezone
from django.db import models
import datetime


# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True, default=datetime.datetime.now) 
    modified_date    = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <  now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    # http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add

    def save(self, *args, **kwargs):
    # On save, update timestamps '''
      if not self.id:
        self.pub_date = datetime.datetime.today()
      self.modified_date = datetime.datetime.today()
      return super(Poll, self).save(*args, **kwargs)
    

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
