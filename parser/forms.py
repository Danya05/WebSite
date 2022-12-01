from .models import Coins
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, Textarea


class CoinsForm(ModelForm):
    class Meta:
        model = Coins
        fields = ['title', 'description', 'capitalization', 'cost', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название монеты'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание монеты'
            }),
            'capitalization': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Капитализация монеты'
            }),
            'cost': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость монеты'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Точное время'
            })

        }
