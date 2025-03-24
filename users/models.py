from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetail(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, related_name="details")
    about_me = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.account.username