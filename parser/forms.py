from .models import Coins
from django.forms import ModelForm


class CoinsForm(ModelForm):
    class Meta:
        model = Coins
        fields = ['title', 'desription', 'capitalization', 'cost']
