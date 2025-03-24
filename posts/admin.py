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
    list_display = ('id', 'headline', 'writer', 'category', 'visibility', 'published_at')
    list_filter = ('visibility', 'category', 'writer', 'published_at')
    search_fields = ('headline', 'body', 'writer__username')
    prepopulated_fields = {'identifier': ('headline',)}
    autocomplete_fields = ('category', 'tags', 'writer')
    raw_id_fields = ('writer',)
    ordering = ('-published_at',)


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentator', 'post', 'commented_at')
    list_filter = ('commented_at', 'post', 'commentator')
    search_fields = ('message', 'commentator__username', 'post__headline')


@admin.register(BlogPostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'liker', 'post', 'liked_at')
    list_filter = ('liked_at',)
    search_fields = ('liker__username', 'post__headline')