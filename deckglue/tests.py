"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta
from django.http import HttpRequest
from django.utils.timezone import utc
from django.test import TestCase
from guardian.models import User
from guardian.shortcuts import assign_perm
from nose.tools import assert_equals
from cardbox.card_model import Card
from cardbox.deck_model import Deck
from deckglue.models import DelayablePractice
from deckglue.views import PracticeDeckList, next_practice_item


def delayCard(dpid):
    dp = DelayablePractice.objects.get(id=dpid)
    dp.next_practice = datetime.utcnow().replace(tzinfo=utc) + timedelta(minutes=1000)
    dp.save()
    return dp

def makeCardDue( dpid, in_minutes):
    dp = DelayablePractice.objects.get(id=dpid)
    dp.next_practice = datetime.utcnow().replace(tzinfo=utc) - timedelta(minutes=in_minutes)
    dp.save()
    return dp

class PracticeDeckListTest(TestCase):
    """
    This is the PracticeDeckList TestSuite
    """
    fixtures = ['test.json']

    def test_get_query_no_decks(self):
        """Check whether no decks are returned when none should be returned"""
        testuser = User.objects.create(username="TestUser", password="1234")
        dl = PracticeDeckList()
        dl.request = HttpRequest()
        dl.request.user = testuser
        lod = dl.get_queryset()
        assert_equals(lod.count(),0)

    def test_get_query_one_deck(self):
        """Check whether decks are returned when they should be returned"""
        dl = PracticeDeckList()
        dl.request = HttpRequest()
        dl.request.user = User.objects.get(username="zirror")
        lod = dl.get_queryset()
        assert_equals(lod.count(),1)

    def test_get_query_percentage_due_0_no_cards(self):
        """Check whether percentage of cards due is 0 when there are no cards in deck"""
        testuser = User.objects.create(username="TestUser", password="1234")
        testdeck = Deck.objects.create(ID=3, title="Test-Deck", description="test")

        assign_perm('view_deck',testuser,testdeck)
        dl = PracticeDeckList()
        dl.request = HttpRequest()
        dl.request.user = testuser
        lod = dl.get_queryset()

        assert_equals(lod[0].due_percentage,0)

    def test_get_query_percentage_due_0_all_cards_learned(self):
        """Check whether percentage of cards due is 0 when all cards have been learned recently"""
        dl = PracticeDeckList()
        dl.request = HttpRequest()
        dl.request.user = User.objects.get(username="zirror")

        delayCard(1)
        delayCard(2)
        lod = dl.get_queryset()

        assert_equals(lod[0].due_percentage,0)

    def test_get_query_percentage_due_100_all_cards_due(self):
        """Check whether percentage of cards due is 100 when all cards are due"""
        dl = PracticeDeckList()
        dl.request = HttpRequest()
        dl.request.user = User.objects.get(username="zirror")

        lod = dl.get_queryset()

        assert_equals(lod[0].due_percentage,100)

class NextPracticeTemplateTest(TestCase):
    """
    Next Practice Template Text Suite
    """
    fixtures = ['test.json']


    def getNextPracticeTemplate(self):
        npi = next_practice_item()
        npi.template_name = "learning/learn_item.html"
        npi.request = HttpRequest()
        npi.request.user = User.objects.get(username="zirror")
        return npi

    def test_get_cards_when_cards_due(self):
        """Returns response for learning when cards are due"""
        npi = npi = self.getNextPracticeTemplate()

        makeCardDue(1,10)
        itms = npi.get(npi.request,deck_id=1)
        text = str(itms.render())

        assert_equals("learning" in text, True)

    def test_get_cards_when_force(self):
        """Returns no carsds left for learning when none are due"""
        npi = self.getNextPracticeTemplate()

        delayCard(1)
        delayCard(2)
        itms = npi.get(npi.request,deck_id=1)

        assert_equals("Herzlichen" in str(itms), True)

    def test_get_cards_when_force(self):
        """Returns response for learning when force mode but no cards"""
        npi = self.getNextPracticeTemplate()

        delayCard(1)
        delayCard(2)
        itms = npi.get(npi.request,deck_id=1,force=True)
        text = str(itms.render())

        assert_equals("learning" in text, True)



class SignalTests(TestCase):
    """
    This is the Signal TestSuite
    """

    fixtures = ['test.json']


    def setUp(self):
        pass


    def test_create_card_signal(self):
        """Check If Practice objects get created via signal"""
        user = User.objects.get(username="zirror")
        delaypractice = DelayablePractice()
        alldue = delaypractice.get_all_due_for_user(user)
        assert_equals(alldue.count(), 2)

    def test_delete_card_signal(self):
        """Check If Practice objects get deleted via signal when card is deleted"""
        user = User.objects.get(username="zirror")
        card = Card.objects.get(ID=1)
        card.delete()
        delaypractice = DelayablePractice()
        alldue = delaypractice.get_all_due_for_user(user)
        assert_equals(alldue.count(), 1)

    def test_delete_user_signal(self):
        """Check If Practice objects get deleted via signal when user is deleted"""
        user = User.objects.get(username="zirror")
        user.delete()
        allDps = DelayablePractice.objects.all()
        assert_equals(allDps.count(), 0)

class DelayablePracticeTest(TestCase):
    """
    This is the DelayablePractice TestSuite
    """

    fixtures = ['test.json']

    def setUp(self):
        pass

    def test_get_all_due_in_card_id_list(self):
        """Check If Get_all_due_in_card_id_list only returns due cards"""
        user = User.objects.get(username="zirror")
        dp = delayCard(1)
        numberOfDueCardsInList = dp.get_all_due_in_card_id_list(user, [1,2]).count()
        assert_equals(numberOfDueCardsInList,1)

    def test_delay_nothing_if_no_cards_are_due(self):
        """Check If nothing gets delayed when no cards are left due"""
        dp_1 = delayCard(1) # make not due
        dp_2 = delayCard(2) # make not due
        time_1 = dp_1.next_practice
        time_2 = dp_2.next_practice
        dp_1.delay()
        dp_2.delay()
        assert_equals(time_1,dp_1.next_practice)
        assert_equals(time_2,dp_2.next_practice)

    def test_delay_after_latest_card_are_due(self):
        """Check If latest due card is in less than 10 minutes, only delay by that much plus one millisecond is done"""
        dp_1 = makeCardDue(1,5) # make due
        dp_2 = makeCardDue(2,3) # make due, but not as due
        pre_delay = dp_1.next_practice > dp_2.next_practice
        dp_1.delay()
        assert_equals(pre_delay,False)
        assert_equals(dp_1.next_practice > dp_2.next_practice,True)

    def test_delay_for_10_min(self):
        """Card gets delayed for 10 minutes, if there is a planned learning after that"""
        makeCardDue(1,20) # make very due
        dp_2 = makeCardDue(2,25) # make even duer
        dp_2.delay()
        assert_equals(dp_2.next_practice > datetime.utcnow().replace(tzinfo=utc),True)