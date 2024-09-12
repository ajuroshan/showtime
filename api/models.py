from django.db import models
from django.contrib.auth.models import User

class Show(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Episode(models.Model):
    show = models.ForeignKey(Show, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='episodes/')
    episode_number = models.IntegerField()

    def __str__(self):
        return f"{self.title} - Episode {self.episode_number}"

class Comment(models.Model):
    episode = models.ForeignKey(Episode, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)  # Add the user field
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.episode.title} at {self.created_at}"