from rest_framework import generics
from .models import Livro
from .serializers import LivroSerializer

class Listar_Livros(generics.ListAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class Listar_Livro_id(generics.RetrieveAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
