from django.db import transaction
from guardian.shortcuts import assign_perm
from sourcereader import AnkiCardSourceReader
from ankiconverter import ankiTupeToTsuneDict
from cardbox.card_model import Card, Deck

class AnkiImporter():

    @transaction.commit_on_success
    def importCollection(self,pathToApkg,user):
        with AnkiCardSourceReader(pathToApkg) as ankireader:
            self._createCollection(ankireader, user)

    def _createDeck(self,deck):
        names = deck['name'].split("::")
        if len(names) > 1:
            return Deck.objects.create(title=names[0], description="-".join(names[1:]))
        return Deck.objects.create(title=names[0], description=names[0])

    def _checkIfCreateDeck(self,current_cardlist):
        return len(current_cardlist) > 0

    def _convertAnkiCardsToTsuneCards(self,cardlist,deck):
        tsuneCards = []
        for card in cardlist:
            tsuneDict = ankiTupeToTsuneDict(card)
            convertedcard = self._createCardObjectFromTsuneDict(tsuneDict,deck)
            tsuneCards.append(convertedcard)
        return tsuneCards

    def _addAllCardsToDeck(self,cardlist,deck):
        return self._convertAnkiCardsToTsuneCards(cardlist,deck)

    def _createCardObjectFromTsuneDict(self,tsuneDict,deck):
        return Card.objects.create(deck=deck,front=tsuneDict["front"], back=tsuneDict["back"])

    def _createCollection(self,ankireader, user):
        deckdict = ankireader.getDictOfAllDecks()
        for deck_id in deckdict.keys():
            current_cardlist=ankireader.getAllCardsForDeck(deck_id)
            if self._checkIfCreateDeck(current_cardlist):
                deck = self._createDeck(deckdict[deck_id])
                tsunecards = self._addAllCardsToDeck(current_cardlist,deck)
                deck.save()
                [card.save() for card in tsunecards]
                self._assignPerms(user,deck)

    def _assignPerms(self,user,deck):
        assign_perm('view_deck',user,deck)
        assign_perm('change_deck',user,deck)
        assign_perm('delete_deck',user,deck)




