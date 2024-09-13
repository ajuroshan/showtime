from rest_framework import serializers
from .models import Show, Episode, Comment, Cast

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'episode', 'user', 'text', 'created_at']

class EpisodeSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Episode
        fields = '__all__'

class CastSerializer(serializers.ModelSerializer):
        class Meta:
            model = Cast
            fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)
    cast = CastSerializer(many=True, read_only=True)

    class Meta:
        model = Show
        fields = '__all__'
