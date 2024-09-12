from rest_framework.routers import DefaultRouter
from .views import ShowViewSet, EpisodeViewSet, CommentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'shows', ShowViewSet)
router.register(r'episodes', EpisodeViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
