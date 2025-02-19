from django.contrib import admin
from .models import Community, Post

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'handle', 'active', 'private')
    search_fields = ('title', 'handle', 'description')
    prepopulated_fields = {'handle': ('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'community', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username', 'community__title', 'content')