from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self): return self.nome

class Livro(models.Model):
    titulo  = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    def __str__(self): return self.titulo


        