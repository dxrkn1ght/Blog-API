from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import BlogPost, BlogComment, BlogPostLike, BlogTag, BlogCategory
from .serializers import (
    BlogPostSerializer, BlogCommentSerializer, BlogPostLikeSerializer,
    BlogTagSerializer, BlogCategorySerializer
)
from .permissions import (
    IsAdminOnly, IsLikeOwnerOrReadOnly, IsAdminOrReadOnly,
    IsPostAuthorOrAdminOrReadOnly, IsCommentAuthorOrPostAuthorOrAdmin
)


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsPostAuthorOrAdminOrReadOnly]


class BlogCommentViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthorOrPostAuthorOrAdmin]


class BlogPostLikeViewSet(viewsets.ModelViewSet):
    queryset = BlogPostLike.objects.all()
    serializer_class = BlogPostLikeSerializer
    permission_classes = [IsAuthenticated, IsLikeOwnerOrReadOnly]


class BlogTagViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogTagSerializer
    permission_classes = [AllowAny]


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [AllowAny]
