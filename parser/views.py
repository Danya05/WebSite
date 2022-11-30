from django.shortcuts import render
from .models import Coins
from .forms import CoinsForm


def parser_home(request):
    coins = Coins.objects.order_by('capitalization')
    return render(request, 'parser/parser_home.html', {'coins': coins})

def create(request):
    form = CoinsForm()

    data = {
        'form': form
    }

    return render(request, 'parser/create.html')
