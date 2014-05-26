"""Defines the Practice Model for keeping track of practice sessions.

"""

from datetime import datetime, timedelta

from django.utils.timezone import utc

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from .algorithm import interval


class Practice(models.Model):
    """This model saves the learning stats of a user linked to a specific item.

    The Practice model uses the :class:`django.contrib.contenttypes.models.ContentType`
    framework to link it to a generic other object. This way, it can be used to keep track of
    learning progress of any other kind of model.

    Attributes:
     content_type (ForeignKey): PK of the learnable object
     object_id (int): ID of the learnable object
     item (GenericForeignKey): Combines the above.
     started_last_viewing (DateTimeField): Starting time of the most recent learning.
     ended_last_viewing (DateTimeField): Ending time of the most recent learning.
     user (User): The user who is practicing.
     next_practice (DateTimeField): Calculated next time of practice.
     times_practice (int): Number of times the item has been practice by the user.
     easy_factor (float): An arbitrary number roughly representing the difficulty of the item for
      the user.

    """
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
        """Uses the :func:`tsune.memorize.algorithm.interval` function to calculate next practice.

        Args:
         rating (int): Rating from 0 (incorrect) to 5 (easiest) of difficulty of item:
             5 - perfect response
             3 - correct response after a hesitation
             1 - correct response recalled with serious difficulty
             0 - incorrect response

        """
        self.times_practiced += 1
        practice_interval, ef = interval(self.times_practiced, rating, self.easy_factor)
        self.delay(minutes=practice_interval*1440) # delay expects the interval in minutes.
        self.easy_factor = ef
        self.save()

    def delay(self, minutes=10):
        """Adds n minutes to next practice.

        """
        self.next_practice = datetime.utcnow().replace(tzinfo=utc) + timedelta(minutes=minutes)
