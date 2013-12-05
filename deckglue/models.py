from django.contrib.auth.models import Permission
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from cardbox.card_model import Card
from cardbox.deck_model import Deck
from guardian.shortcuts import assign_perm, get_users_with_perms
from guardian.models    import UserObjectPermission
from memorize.models import Practice
from django.contrib.auth.models import User

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

