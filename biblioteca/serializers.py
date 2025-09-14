from rest_framework import serializers
from .models import Livro

class LivroSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField()
    genero = serializers.StringRelatedField()

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'genero', 'ano_publicacao', 'sinopse']
