from rest_framework import serializers
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Genre model.
    """
    class Meta:
        model = Genre
        fields = '__all__'
