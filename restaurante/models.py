from django.db import models


class PromocaoEvento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='promocoes/')

    def __str__(self):
        return self.titulo


class TipoPrato(models.TextChoices):
    ENTRADA = 'EN', 'Entrada'
    PRINCIPAL = 'PR', 'Prato Principal'
    SOBREMESA = 'SO', 'Sobremesa'

class CardapioItem(models.Model):
    tipo = models.CharField(
        max_length=2,
        choices=TipoPrato.choices
    )
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='cardapio/')
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.titulo

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='equipe/')
    
    def __str__(self):
        return self.nome

class FeedbackCliente(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField("Avaliação")
    foto = models.ImageField(upload_to='historia/', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - historia"
