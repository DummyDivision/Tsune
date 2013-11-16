from django.db import models
from django.core.urlresolvers import reverse
import cardbox.card_model

class Deck(models.Model):
    ID = models.AutoField(primary_key=True)
    # Cards are realized as Many to Many in the card model
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (('view_deck', 'Can view deck'),)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the unique url to this object"""
        return reverse('deck:deck_detail', kwargs={'pk': self.ID})

    def get_total_cards(self):
        return cardbox.card_model.Card.objects.filter(deck = self.ID).count()