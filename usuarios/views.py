from django.shortcuts import render, redirect
from django.contrib.auth import login
from biblioteca.models import Livro
from .forms import UsuarioCadastroForm

def cadastro_usuario(request):
    if request.method == "POST":
        form = UsuarioCadastroForm(request.POST)
        if form.is_valid():
            user = form.save()         # Salva o usuário no banco
            login(request, user)       # Loga o usuário automaticamente
            return redirect('livros')  # Redireciona para a página de livros
    else:
        form = UsuarioCadastroForm()
    
    return render(request, 'usuarios/cadastro.html', {'form': form})

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})
