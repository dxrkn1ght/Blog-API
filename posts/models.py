from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)
    identifier = models.SlugField(unique=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class BlogTag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    identifier = models.SlugField(unique=True)

    def __str__(self):
        return self.title



class BlogPost(models.Model):
    headline = models.CharField(max_length=200)
    identifier = models.SlugField(unique=True)
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(BlogTag, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=10, choices=[("draft", "Draft"), ("published", "Published")], default="draft")
    cover_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.headline



class BlogPostLike(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'liker')

    def __str__(self):
        return f"{self.liker.username} liked {self.post.headline}"


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.commentator.username} - {self.post.headline}"
