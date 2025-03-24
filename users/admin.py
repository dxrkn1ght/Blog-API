from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserDetail


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
