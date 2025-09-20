from django.db import models
from decimal import Decimal

class Vantagem(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição da Vantagem")

    class Meta:
        verbose_name = "Vantagem"
        verbose_name_plural = "Vantagens"

    def __str__(self):
        return self.descricao


class Plano(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Plano", unique=True)
    preco_inicial = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Preço Inicial")
    preco_recorrente = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Preço Recorrente")
    usuarios_max = models.IntegerField(default=1, verbose_name="Número máximo de usuários")
    duracao_meses = models.IntegerField(default=1, verbose_name="Duração do Plano (meses)")
    ativo = models.BooleanField(default=True, verbose_name="Plano Ativo")
    vantagens = models.ManyToManyField(Vantagem, related_name="planos", blank=True, verbose_name="Vantagens")
    imagem = models.ImageField(upload_to='planos/', blank=True, null=True, verbose_name="Imagem/Ícone do Plano")

    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def preco_formatado(self):
        return f"Inicial: R${self.preco_inicial} | Recorrente: R${self.preco_recorrente}"

    def save(self, *args, **kwargs):
        """Define os preços automaticamente com base no nome do plano"""
        if self.nome == "Gratuito":
            self.preco_inicial = Decimal('0.00')
            self.preco_recorrente = Decimal('0.00')
        elif self.nome == "Duo":
            self.preco_inicial = Decimal('19.90')
            self.preco_recorrente = Decimal('29.90')
        elif self.nome == "Angelical":
            self.preco_inicial = Decimal('29.90')
            self.preco_recorrente = Decimal('49.90')
        super().save(*args, **kwargs)
