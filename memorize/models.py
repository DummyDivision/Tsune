from datetime import datetime, timedelta
import datetime
from django.utils.timezone import utc

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from .algorithm import interval


class Practice(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    item = generic.GenericForeignKey('content_type', 'object_id')
    started_last_viewing = models.DateTimeField(null=True,blank=True, auto_now_add=True)
    ended_last_viewing = models.DateTimeField(null=True,blank=True, auto_now_add=True)
    user = models.ForeignKey(User)
    next_practice = models.DateTimeField(auto_now_add=True)
    times_practiced = models.PositiveIntegerField(default=0)
    easy_factor = models.FloatField(default=2.5)

    class Meta:
        ordering = ['next_practice']

    def set_next_practice(self, rating):
        self.times_practiced += 1
        minutes, ef = interval(self.times_practiced, rating, self.easy_factor)
        self.next_practice = datetime.datetime.utcnow().replace(tzinfo=utc) + timedelta(minutes=minutes)
        self.easy_factor = ef

    def delay(self):
        self.next_practice = datetime.utcnow().replace(utc) + timedelta(minutes=10)
