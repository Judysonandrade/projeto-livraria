from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('livros/', views.livros, name='livros'),
    path('livros/<int:pk>/', LivroDetailView.as_view(), name='livro_detalhes'),
]
