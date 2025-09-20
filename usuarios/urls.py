from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('livros/', views.lista_livros, name='livros'),
]
