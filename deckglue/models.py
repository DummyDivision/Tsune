from django.contrib.auth.models import Permission
from django.db.models.aggregates import Max
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from cardbox.card_model import Card
from cardbox.deck_model import Deck
from guardian.shortcuts import assign_perm, get_users_with_perms
from guardian.models    import UserObjectPermission
from memorize.models import Practice
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils.timezone import utc
from django.db import models

@receiver(post_save, sender=UserObjectPermission)
def create_practice_objects_for_new_viewers(sender, **kwargs):
    if kwargs['instance'].permission_id == Permission.objects.get(codename="view_deck").id:
        for card in Card.objects.filter(deck=kwargs['instance'].object_pk):
            Practice(item=card, user=User.objects.get(id = kwargs['instance'].user_id)).save()

@receiver(pre_delete, sender=UserObjectPermission)
def delete_practice_objects_for_removed_viewers(sender, **kwargs):
    if kwargs['instance'].permission_id == Permission.objects.get(codename="view_deck").id:
        for card in Card.objects.filter(deck=kwargs['instance'].object_pk):
            Practice.objects.get(object_id=card.ID, user=User.objects.get(id = kwargs['instance'].user_id)).delete()

@receiver(post_save, sender=Card)
def create_practice_objects_for_new_card(sender,update_fields, **kwargs):
    """Creates practice objects for all users with permission to view the card.

    """
    perm_users = get_users_with_perms(kwargs['instance'].deck)
    for user in perm_users:
        practice = Practice(item = kwargs['instance'], user = user)
        if Practice.objects.filter(object_id = kwargs['instance'].ID, user=user).count() == 0:
            practice.save()



@receiver(pre_delete, sender=Card)
def delete_practice_objects(sender, **kwargs):
    """Deletes all practice objects for a card once it is deleted.

    """
    Practice.objects.filter(object_id = kwargs['instance'].ID).delete()

class DelayablePractice(Practice):
    class Meta:
        proxy = True

    def get_all_due_for_user(self, user):
        """Returns all practices which are due for user.

        """
        return DelayablePractice.objects.filter(user=user, next_practice__lte=datetime.utcnow().replace(tzinfo=utc))

    def get_all_due_in_card_id_list(self, user, cardlist):
        """Returns all practices which are due for user among cards in cardlist.

        """
        return self.get_all_due_for_user(user).filter(object_id__in=cardlist)

    def delay(self):
        """Delays card for review in this session.

        This function delays the next practice until either 10 minutes are up or the end of the session is
        reached, whichever comes first.

        """
        now = datetime.utcnow().replace(tzinfo=utc)
        all_due_cards_in_deck = self.get_all_due_in_card_id_list(self.user, Card.objects.filter(deck=self.item.deck))

        #Don't delay if no cards left are due
        if all_due_cards_in_deck.count() is 0:
            return
        latest_due_practice = all_due_cards_in_deck.aggregate(Max('next_practice'))['next_practice__max']
        if (latest_due_practice-now).min < timedelta(minutes=10):
            self.next_practice = latest_due_practice + timedelta(milliseconds=1)
        else:
            self.next_practice = now + timedelta(minutes=10)


