from django.shortcuts import render, redirect
from .models import Coins
from .forms import CoinsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def parser_home(request):
    coins = Coins.objects.order_by('-capitalization')
    return render(request, 'parser/parser_home.html', {'coins': coins})


class CoinsDetailView(DetailView):
    model = Coins
    template_name = 'parser/details_view.html'
    context_object_name = 'coin'


class CoinsUpdateView(UpdateView):
    model = Coins
    template_name = 'parser/create.html'
    form_class = CoinsForm


class CoinsDeleteView(DeleteView):
    model = Coins
    success_url = '/parser/'
    template_name = 'parser/coins_delete.html'


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

