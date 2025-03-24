from django.contrib import admin
from .models import BlogCategory, BlogTag, BlogPost, BlogPostLike, BlogComment


@admin.register(BlogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'identifier')
    search_fields = ('title',)
    prepopulated_fields = {'identifier': ('title',)}


@admin.register(BlogTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'identifier')
    search_fields = ('title',)
    prepopulated_fields = {'identifier': ('title',)}


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline', 'writer', 'category', 'status', 'published_at')
    list_filter = ('status', 'category', 'writer', 'published_at')
    search_fields = ('headline', 'content', 'writer__username')
    prepopulated_fields = {'slug': ('headline',)}
    autocomplete_fields = ('category', 'tags', 'writer')
    raw_id_fields = ('writer',)
    ordering = ('-published_at',)


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at')
    list_filter = ('created_at', 'post', 'author')
    search_fields = ('content', 'author__username', 'post__title')


@admin.register(BlogPostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentator', 'message', 'value', 'commented_at')
    list_filter = ('value', 'commented_at')
    search_fields = ('commentator__username', 'post__title')
