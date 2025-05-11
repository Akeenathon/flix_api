from rest_framework import serializers
from .models import Actor


class ActorSeralizer(serializers.ModelSerializer):
    """
    Serializer for the Actor model.
    """
    class Meta:
        model = Actor
        fields = '__all__'
