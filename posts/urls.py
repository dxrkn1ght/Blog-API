from os.path import basename

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, BlogCommentViewSet, BlogPostLikeViewSet, BlogTagViewSet, BlogCategoryViewSet


router = DefaultRouter()
router.register(r'posts', BlogPostViewSet, basename='post')
router.register(r'comments', BlogCommentViewSet, basename='comment')
router.register(r'likes', BlogPostLikeViewSet, basename='post-like')
router.register(r'tags', BlogTagViewSet, basename='tag')
router.register(r'categories', BlogCategoryViewSet, basename='category')


urlpatterns = [
    path('api/', include(router.urls)),
]
