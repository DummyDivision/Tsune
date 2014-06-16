from django.contrib.auth.models import Permission
from django.db.models.aggregates import Max
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from cardbox.card_model import Card
from guardian.shortcuts import get_users_with_perms
from guardian.models    import UserObjectPermission
from memorize.algorithm import interval
from memorize.models import Practice
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils.timezone import utc
from profiles.models import Profile


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


@receiver(post_save, sender=User)
def create_profile_for_new_user(sender,update_fields, **kwargs):
    """Creates a profile for a new user. Fills default nickname value."""
    if Profile.objects.filter(user=kwargs['instance']).count() is 0 :
        Profile.objects.create(user=kwargs['instance'], nickname=kwargs['instance'].email.split('@')[0])


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

    def delay(self, minutes=10):
        """Delays card for review in this session.
        This function delays the next practice by the given amount of minutes.
        """
        now = datetime.utcnow().replace(tzinfo=utc)
        self.next_practice = now + timedelta(minutes=minutes)

    def set_next_practice(self, rating):
        """Uses the :func:`tsune.memorize.algorithm.interval` function to calculate next practice.
        Args:
         rating (int): Rating from 0 (incorrect) to 5 (easiest) of difficulty of item:
             5 - perfect response
             3 - correct response after a hesitation
             1 - correct response recalled with serious difficulty
             0 - incorrect response
        """
        if rating == 0:
            self.times_practiced = 0
        else:
            self.times_practiced += 1
        repetition_interval, self.easy_factor = interval(self.times_practiced, rating, self.easy_factor)
        self.delay(minutes=repetition_interval)
        self.save()