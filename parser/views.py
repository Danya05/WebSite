from django.shortcuts import render

def parser_home(request):
    return render(request, 'parser/parser_home.html')
