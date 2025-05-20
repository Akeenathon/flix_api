from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaulPermission
from .models import Review
from .serializers import ReviewSeralizer


class ReviewListCreateView(generics.ListCreateAPIView):
    """
    API View para listar e criar avaliações.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSeralizer
    permission_classes = [IsAuthenticated, GlobalDefaulPermission]


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Api View para detalhar, atualizar e deletar avaliações.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSeralizer
    permission_classes = [IsAuthenticated, GlobalDefaulPermission]
