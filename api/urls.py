from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'shows', ShowViewSet)
router.register(r'episodes', EpisodeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'cast', CastViewSet)

urlpatterns = [
    path('shows/search/', ShowSearchView.as_view(), name='show-search'),  # Show search URL
    path('episodes/search/', EpisodeSearchView.as_view(), name='episode-search'),  # Episode search URL
    path('', include(router.urls)),
]
