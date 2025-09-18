from django.shortcuts import render
from .models import PromocaoEvento, CardapioItem

def promocoes(request):
    dados = PromocaoEvento.objects.all()
    return render(request, 'restaurante/promocoes.html', {'dados': dados})

def cardapio(request):
    itens = CardapioItem.objects.all()
    return render(request, 'restaurante/cardapio.html', {'itens': itens})
