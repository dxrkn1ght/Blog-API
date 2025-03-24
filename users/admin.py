from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserDetail

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = UserDetail
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(UserDetail)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('account', 'about_me', 'homepage')
    search_fields = ('account__username', 'about_me')