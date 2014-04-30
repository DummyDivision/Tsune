from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from guardian.models import User
from models import Profile


class ProfileView(DetailView):
    model = Profile