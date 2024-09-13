from rest_framework import viewsets
from .models import Show, Episode, Comment, Cast
from .serializers import ShowSerializer, EpisodeSerializer, CommentSerializer, CastSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, filters


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can comment

    def perform_create(self, serializer):
        # Set the user to the logged-in user
        serializer.save(user=self.request.user)


class ShowSearchView(generics.ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']  # Search shows by title or description

# Search view for episodes
class EpisodeSearchView(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'show__title']

class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer