from rest_framework import serializers
from .models import ArenaCards
from .models import PopularCards
from .models import Decks
from .models import DeckCards

class ArenaCardsSerializer(serializers.ModelSerializer):
   """Serializer to map the Model instance into JSON format."""

   class Meta:
      """Meta class to map serializer's fields with the model fields."""
      model = ArenaCards
      fields = ('id', 'title', 'percentage', 'cards')

class PopularCardsSerializer(serializers.ModelSerializer):
   """Serializer to map the Model instance into JSON format."""
   cards = serializers.ListField(
      child=serializers.DictField())
   class Meta:
      """Meta class to map serializer's fields with the model fields."""
      model = PopularCards
      fields = '__all__'

class DecksSerializer(serializers.ModelSerializer):
   """Serializer to map the Model instance into JSON format."""

   class Meta:
      """Meta class to map serializer's fields with the model fields."""
      model = Decks
      fields = ('id', 'title', 'place', 'img')

class DeckCardsSerializer(serializers.ModelSerializer):
   """Serializer to map the Model instance into JSON format."""
   popularCards = serializers.ListField(
      child=serializers.DictField())
   
   decks = serializers.ListField(
      child=serializers.DictField())

   class Meta:
      """Meta class to map serializer's fields with the model fields."""
      model = DeckCards
      fields = ('popularCards', 'decks')