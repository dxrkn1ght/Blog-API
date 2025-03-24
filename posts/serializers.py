from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogCategory, BlogTag, BlogPost, BlogComment, BlogPostLike


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug', 'description']


class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ['id', 'name', 'slug']


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = BlogCategorySerializer()
    tags = BlogTagSerializer(many=True)
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'content', 'author', 'category', 'tags',
            'created_at', 'updated_at', 'status', 'featured_image', 'total_likes', 'total_comments'
        ]

    def get_total_likes(self, obj):
        return obj.likes.count()

    def get_total_comments(self, obj):
        return obj.comments.count()


class BlogCommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.PrimaryKeyRelatedField(queryset=BlogPost.objects.all())

    class Meta:
        model = BlogComment
        fields = ['id', 'post', 'author', 'content', 'created_at']


class BlogPostLikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.PrimaryKeyRelatedField(queryset=BlogPost.objects.all())

    class Meta:
        model = BlogPostLike
        fields = ['id', 'post', 'user', 'created_at']
