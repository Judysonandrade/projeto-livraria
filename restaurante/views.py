from django.shortcuts import render
from datetime import datetime
from .models import PromocaoEvento, CardapioItem, Funcionario, FeedbackCliente, Reserva, FaleConosco, Especialidades

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

def criar_reserva(request):
    if request.method == "POST":
        try:
            datetime_str = request.POST.get('data_reserva') 

            dt_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M")

            data = dt_obj.date()
            hora = dt_obj.time()

            Reserva.objects.create(
                nome_cliente=request.POST.get('nome_cliente'),
                telefone=request.POST.get('telefone'),
                data_reserva=data,
                hora_reserva=hora,
                numero_pessoas=request.POST.get('numero_pessoas'),
                tipo_reserva=request.POST.get('tipo_reserva', '')
            )
            mensagem = "Reserva criada com sucesso!"
        except Exception as e:
            mensagem = f"Erro: {e}"
    else:
        mensagem = None

    reservas = Reserva.objects.all()
    return render(request, 'restaurante/reservar.html', {
        'reservas': reservas,
        'mensagem': mensagem
    })
 

def fale_conosco(request):
    mensagem = None
    if request.method == "POST":
        try:
            fale = FaleConosco.objects.create(
                nome=request.POST.get('nome'),
                telefone=request.POST.get('telefone'),
                mensagem=request.POST.get('mensagem', '')
            )
            fale.save()
            mensagem = "Mensagem enviada com sucesso!"
        except Exception as e:
            mensagem = f"Erro ao enviar mensagem: {e}"

    mensagens = FaleConosco.objects.all()
    return render(request, 'restaurante/faleconosco.html', {
        'mensagens': mensagens,
        'mensagem': mensagem
    })

def especialidades(request):
    dados = Especialidades.objects.all()
    return render(request, 'restaurante/especialidades.html', {'especialidades': dados})

def executivo(request):
    itens_selecionados = CardapioItem.objects.filter(selecionado=True)
    return render(request, 'restaurante/executivo.html', {'itens': itens_selecionados})
