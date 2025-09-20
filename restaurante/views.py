from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PromocaoEvento, CardapioItem, Funcionario, FeedbackCliente, Reserva, FaleConosco

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


@api_view(['POST'])
def criar_reserva(request):
    try:
        reserva = Reserva.objects.create(
            nome_cliente=request.data.get('nome_cliente'),
            telefone=request.data.get('telefone'),
            data_reserva=request.data.get('data_reserva'),
            hora_reserva=request.data.get('hora_reserva'),
            numero_pessoas=request.data.get('numero_pessoas'),
            tipo_reserva=request.data.get('tipo_reserva', '')
        )
        reserva.save()
        return Response({
            "id": reserva.id,
            "nome_cliente": reserva.nome_cliente,
            "telefone": reserva.telefone,
            "data_reserva": reserva.data_reserva,
            "hora_reserva": reserva.hora_reserva,
            "numero_pessoas": reserva.numero_pessoas,
            "tipo_reserva": reserva.tipo_reserva
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def fale_conosco(request):
    try:
        faleConosco = FaleConosco.objects.create(
            nome=request.data.get('nome'),
            telefone=request.data.get('telefone'),
            mensagem=request.data.get('mensagem', '')
        )
        faleConosco.save()
        return Response({
            "id": faleConosco.id,
            "nome": faleConosco.nome,
            "telefone": faleConosco.telefone,
            "mensagem": faleConosco.mensagem
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
