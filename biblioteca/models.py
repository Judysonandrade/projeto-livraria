from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Gênero")

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"
        ordering = ['nome']

    def __str__(self): return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self): return self.nome

class Livro(models.Model):
    titulo  = models.CharField(max_length=200, verbose_name="Título do Livro")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor do Livro")
    sinopse = models.TextField(verbose_name="Sinopse")
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, related_name='books', verbose_name="Gênero")
    ano_publicacao = models.IntegerField(verbose_name="Ano de Publicação")
    capa_image = models.ImageField(upload_to='capas/', blank=True, null=True, verbose_name="Capa do Livro")

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ['titulo']

    def __str__(self): return self.titulo


        