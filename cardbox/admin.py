from django.contrib import admin
from deck_model import Deck
from card_model import Card
from guardian.admin import GuardedModelAdmin

admin.site.register(Deck, GuardedModelAdmin)
admin.site.register(Card)