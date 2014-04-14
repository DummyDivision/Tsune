from django.forms import Textarea, ModelForm
from card_model import Card
from markitup.widgets import MarkItUpWidget

class CardForm(ModelForm):
    """The basic form for updating or editing cards"""

    class Meta:
        model = Card
        fields = ('front', 'back', 'deck')
        widgets = {
            'front': MarkItUpWidget(attrs={'class': "form-control"}), #Textarea(attrs={'class': "form-control"}),
            'back': MarkItUpWidget(attrs={'class': "form-control"}),
        }
