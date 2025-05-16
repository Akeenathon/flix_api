from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateView(generics.ListCreateAPIView):
    """
    API view para listar e criar atores.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    #permission_classes = [IsAuthenticated]


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view para detalhar, atualizar ou deletar atores.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    #permission_classes = [IsAuthenticated]
