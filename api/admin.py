from django.contrib import admin
from .models import Show, Episode, Comment
# Register your models here.

@admin.register(Show)
class ModelNameAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title', 'description']
	list_filter = ['title']
	list_per_page = 10

@admin.register(Episode)
class ModelNameAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title', 'description', 'episode_number']
	list_filter = ['title']
	list_per_page = 10


@admin.register(Comment)
class ModelNameAdmin(admin.ModelAdmin):
	search_fields = ['text']
	list_display = ['text', 'created_at']
	list_filter = ['text']
	list_per_page = 10

