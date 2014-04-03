# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, FormView
from django.contrib.auth import views
from tsune  import settings

def login(request,**kwargs):
    response = views.login(request,kwargs.get('template_name'));
    response.context_data['secrets_present'] = settings.SECRETS_PRESENT;
    return response;