from django.contrib import admin
from .models import Community, Post, Comment, Reaction

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'handle', 'active', 'private')
    search_fields = ('title', 'handle', 'description')
    prepopulated_fields = {'handle': ('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'community', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username', 'community__title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_object', 'created_at', 'updated_at')
    search_fields = ('author__username', 'comment', 'content_object__title')

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('author', 'reaction', 'content_object', 'created_at', 'updated_at')
    search_fields = ('author__username', 'reaction', 'content_object__title')