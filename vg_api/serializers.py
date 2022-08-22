from rest_framework import serializers
from .models import Game
from django.contrib.auth.models import User

#Serializer for game data model
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'release_date', 'publisher', 'developer', 'critic_rating',\
        'user_rating', 'platforms', 'genres', 'image_url', 'created', 'owner']
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'games']