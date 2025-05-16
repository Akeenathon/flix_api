from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Actor
from .serializers import ActorSeralizer


class ActorListCreateView(generics.ListCreateAPIView):
    """
    API view para listar e criar atores.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSeralizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        nacionality = self.request.query_params.get('nacionality', None)
        if nacionality is not None:
            queryset = queryset.filter(nacionality=nacionality)
        return queryset


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view para detalhar, atualizar ou deletar atores.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSeralizer
    permission_classes = [IsAuthenticated]
