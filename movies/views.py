from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from . models import Movie
from . serializers import MovieSerializer, MovieGetSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    """
    API view para listar e criar filmes.
    """
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        """
        Retorna o serializador apropriado com base no método da request.
        """
        if self.request.method == 'GET':
            return MovieGetSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view para detalhar, atualizar ou deletar um filme.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


class MovieStatsView(views.APIview):
    """
    API view para obter estatísticas de filmes.
    """
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()

    def get(self, request):
        """
        Obtendo estatísticas de filmes.
        """
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'average_stars': round(average_stars, 1) if average_stars else 0,
            }, status=status.HTTP_200_OK)
