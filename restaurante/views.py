from django.shortcuts import render
from .models import PromocaoEvento, CardapioItem, Funcionario, FeedbackCliente

def promocoes(request):
    dados = PromocaoEvento.objects.all()
    return render(request, 'restaurante/promocoes.html', {'dados': dados})

def cardapio(request):
    itens = CardapioItem.objects.all()
    return render(request, 'restaurante/cardapio.html', {'itens': itens})

def equipe(request):
    equipe = Funcionario.objects.all()
    return render(request, 'restaurante/equipe.html', {'equipe': equipe})

def feedbacks(request):
    feedbacks = FeedbackCliente.objects.all()
    return render(request, 'restaurante/feedbacks.html', {'feedbacks': feedbacks})
