from django.contrib import admin
from .models import Show, Episode, Comment, Cast
# Register your models here.

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title', 'description']
	list_filter = ['title','episodes']
	list_per_page = 10

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title', 'description', 'episode_number']
	list_filter = ['title']
	list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	search_fields = ['text']
	list_display = ['text', 'created_at']
	list_filter = ['text']
	list_per_page = 10

@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['name', 'role']
	list_filter = ['name']
	list_per_page = 10
