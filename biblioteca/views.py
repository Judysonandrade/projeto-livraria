from django.shortcuts import render, get_object_or_404
from .models import Livro

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})

def detalhe_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'biblioteca/detalhe_livro.html', {'livro': livro})
