from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/<int:pk>/', views.detalhe_livro, name='detalhe_livro'),
    
]
