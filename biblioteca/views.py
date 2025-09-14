from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [] 
        return [IsAdminUser()]
