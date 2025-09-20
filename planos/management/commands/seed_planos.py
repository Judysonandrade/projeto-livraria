from django.core.management.base import BaseCommand
from decimal import Decimal
from planos.models import Plano, Vantagem

class Command(BaseCommand):
    help = 'Cria planos e vantagens iniciais'

    def handle(self, *args, **options):
        vantagens = ['Curadoria especializada', 'Comunidade integrada', 'Economia', 'Descobertas']
        v_objs = [Vantagem.objects.get_or_create(descricao=v)[0] for v in vantagens]

        planos_data = [
            {'nome': 'Gratuito', 'preco_inicial': Decimal('0.00'), 'preco_recorrente': Decimal('0.00'), 'vantagens': []},
            {'nome': 'Duo', 'preco_inicial': Decimal('19.90'), 'preco_recorrente': Decimal('29.90'), 'vantagens': []},
            {'nome': 'Angelical', 'preco_inicial': Decimal('29.90'), 'preco_recorrente': Decimal('49.90'), 'vantagens': v_objs},
        ]

        for p in planos_data:
            plano, created = Plano.objects.get_or_create(nome=p['nome'], defaults={
                'preco_inicial': p['preco_inicial'],
                'preco_recorrente': p['preco_recorrente'],
            })
            if p['vantagens']:
                plano.vantagens.set(p['vantagens'])

        self.stdout.write(self.style.SUCCESS('Planos e vantagens criados/atualizados com sucesso!'))


        