# TODO: Connection with deck
from django.db import models
from django.core.urlresolvers import reverse
from cardbox.deck_model import Deck


class Card(models.Model):
    ID = models.AutoField(primary_key=True)
    deck = models.ForeignKey(Deck)
    front = models.CharField(max_length=512)
    back = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.front

    def get_absolute_url(self):
        """Returns the unique url to this object"""
        return reverse('card:card_detail', kwargs={'pk': self.ID})