from django.contrib import admin
from card_model import Card, Deck
from guardian.admin import GuardedModelAdmin

admin.site.register(Deck, GuardedModelAdmin)
admin.site.register(Card)