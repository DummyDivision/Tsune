from django.forms import Textarea, ModelForm
from card_model import Card


class CardForm(ModelForm):
    """The basic form for updating or editing cards"""

    class Meta:
        model = Card
        fields = ('front', 'back')
        widgets = {
            'front': Textarea(attrs={'class': "form-control"}),
            'back': Textarea(attrs={'class': "form-control"}),

        }
