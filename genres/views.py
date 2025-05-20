from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaulPermission
from .models import Genre
from .serializers import GenreSerializer


class GenreListCreateView(generics.ListCreateAPIView):
    """
    API view para listar e criar novos gêneros.
    """
    permission_classes = [IsAuthenticated, GlobalDefaulPermission]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view para detalhar, atualizar ou deletar um gênero.
    """
    permission_classes = [IsAuthenticated, GlobalDefaulPermission]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
