from django.shortcuts import render, redirect
from .models import Coins
from .forms import CoinsForm


def parser_home(request):
    coins = Coins.objects.order_by('capitalization')
    return render(request, 'parser/parser_home.html', {'coins': coins})


def create(request):
    error = ''
    if request.method == 'POST':
        form = CoinsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parser_home')
        else:
            error = 'Введите верные данные'

    form = CoinsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'parser/create.html', data)
