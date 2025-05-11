from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from models import Genre
from serializers import GenreSerializer


class GenreListCreateView(generics.ListCreateAPIView):
    """
    API view to list and create genres.
    """
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a genre.
    """
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
