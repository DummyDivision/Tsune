from django.forms import ModelForm
from django.forms.widgets import Textarea, TextInput
from deck_model import Deck

class DeckForm(ModelForm):
    """The basic form for updating or editing decks"""

    class Meta:
        model = Deck
        fields = ('title', 'description')
        widgets = {
            'title': TextInput(attrs={'class': "form-control"}),
            'description': Textarea(attrs={'class': "form-control"})
        }