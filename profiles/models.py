from django.db import models
from django.contrib.auth.models import User
from markitup.fields import MarkupField


class Profile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    nickname = models.CharField(max_length=20)
    description = MarkupField()
    image_url = models.URLField()