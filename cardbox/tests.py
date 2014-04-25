"""
.. module:: tests
    :platform: Unix, Windows
    :synopsis: A useful model indeed.

.. moduleauthor:: Andreas Waigand <awaigand@gmx.net>

"""
from django.http import HttpRequest

from django.test import TestCase
from guardian.models import User
from nose.tools import assert_equals
from cardbox.card_model import Card
from cardbox.deck_model import Deck
from guardian.shortcuts import assign_perm
from cardbox.deck_views import DeckList


class CardModelTests(TestCase):
    """
     This is the CardModelTest Suite
    """

    def setUp(self):
        testdeck = Deck.objects.create(ID=1, title="Test-Deck", description="test")
        Card.objects.create(deck=testdeck, front="#Test", back="#Test")

    def test_auto_markup_transformation(self):
        """Check If Markup Transformation works"""
        assert_equals(Card.objects.get(ID=1).front.rendered, "<h1>Test</h1>")

class DeckViewTests(TestCase):
    """
     This is the DeckViewTest Suite
    """

    def setUp(self):
        testuser = User.objects.create(username="TestUser", password="1234")
        testdeck = Deck.objects.create(ID=1, title="Test-Deck", description="test")
        seconddeck = Deck.objects.create(ID=2, title="Second-Deck", description="test")
        Card.objects.create(deck=testdeck, front="#Test", back="#Test")
        Card.objects.create(deck=testdeck, front="#Test", back="#Test")
        Card.objects.create(deck=seconddeck, front="#Test", back="#Test")
        assign_perm('view_deck',testuser,testdeck)


    def test_deckList_getList(self):
        """
        Test DeckList Views getList
        """
        t = DeckList()
        t.request = HttpRequest()
        t.request.user = User.objects.get(username="TestUser")
        decklist = t.queryset()
        assert_equals(Deck.objects.get(ID=1) in decklist, True)


class DeckModelTests(TestCase):
    """
    This is the DeckModelTest Suite
    """

    def setUp(self):
        testdeck = Deck.objects.create(ID=1, title="Test-Deck", description="test")
        Card.objects.create(deck=testdeck, front="#Test", back="#Test")
        Card.objects.create(deck=testdeck, front="#Test", back="#Test")
        Card.objects.create(deck=testdeck, front="#Test", back="#Test")

    def test_get_total_cards(self):
        """Check If Deck Model Method get_total_cards returns number of cards in deck"""
        assert_equals(Deck.objects.get(ID=1).get_total_cards(), 3)