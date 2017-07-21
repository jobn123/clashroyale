from rest_framework import serializers
from .models import ArenaCards

class ArenaCardsSerializer(serializers.ModelSerializer):
   """Serializer to map the Model instance into JSON format."""

   class Meta:
      """Meta class to map serializer's fields with the model fields."""
      model = ArenaCards
      fields = ('id', 'title', 'percentage', 'cards')