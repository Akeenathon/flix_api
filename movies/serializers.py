from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_data', 'resume', 'actors', 'genres')

    def validate_date_release(self, value):
        if value.year < 1970:
            raise serializers.ValidationError("A data do filme deve ser superior à 1970.")
        return value

    def validate_resume(self, value):
        if len(value) < 500:
            raise serializers.ValidationError("O resumo deve ter menos de 500 caracteres.")
        return value


class MovieGetSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.ratings.aggregate(Avg('stars'))['rating__avg']

        if rate:
            return round(rate, 1)

        return None
