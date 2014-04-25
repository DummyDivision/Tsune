"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta
from django.utils.timezone import utc
from django.test import TestCase
from guardian.models import User
from nose.tools import assert_equals
from cardbox.card_model import Card
from cardbox.deck_model import Deck
from deckglue.models import DelayablePractice
from memorize.models import Practice



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
        all = DelayablePractice.objects.all()
        assert_equals(all.count(), 0)

class DelayablePracticeTest(TestCase):
    """
    This is the DelayablePractice TestSuite
    """

    fixtures = ['test.json']

    def setUp(self):
        pass

    def delayCard(self, dpid):
        dp = DelayablePractice.objects.get(id=dpid)
        dp.next_practice = datetime.utcnow().replace(tzinfo=utc) + timedelta(minutes=1000)
        dp.save()
        return dp

    def makeCardDue(self, dpid, in_minutes):
        dp = DelayablePractice.objects.get(id=dpid)
        dp.next_practice = datetime.utcnow().replace(tzinfo=utc) - timedelta(minutes=in_minutes)
        dp.save()
        return dp

    def test_get_all_due_in_card_id_list(self):
        """Check If Get_all_due_in_card_id_list only returns due cards"""
        user = User.objects.get(username="zirror")
        dp = self.delayCard(1)
        numberOfDueCardsInList = dp.get_all_due_in_card_id_list(user, [1,2]).count()
        assert_equals(numberOfDueCardsInList,1)

    def test_delay_nothing_if_no_cards_are_due(self):
        """Check If nothing gets delayed when no cards are left due"""
        user = User.objects.get(username="zirror")
        dp_1 = self.delayCard(1) # make not due
        dp_2 = self.delayCard(2) # make not due
        time_1 = dp_1.next_practice
        time_2 = dp_2.next_practice
        dp_1.delay()
        dp_2.delay()
        assert_equals(time_1,dp_1.next_practice)
        assert_equals(time_2,dp_2.next_practice)

    def test_delay_after_latest_card_are_due(self):
        """Check If latest due card is in less than 10 minutes, only delay by that much plus one millisecond is done"""
        dp_1 = self.makeCardDue(1,5) # make due
        dp_2 = self.makeCardDue(2,3) # make due, but not as due
        pre_delay = dp_1.next_practice > dp_2.next_practice
        dp_1.delay()
        assert_equals(pre_delay,False)
        assert_equals(dp_1.next_practice > dp_2.next_practice,True)

    def test_delay_for_10_min(self):
        """Card gets delayed for 10 minutes, if """
        dp_1 = self.makeCardDue(1,20) # make very due
        dp_2 = self.makeCardDue(2,25) # make due, but not as due
        dp_2.delay()
        assert_equals(dp_2.next_practice > datetime.utcnow().replace(tzinfo=utc),True)