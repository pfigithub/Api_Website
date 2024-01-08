from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_superuser", "is_active", "is_verified")
    list_filter = ("email", "is_staff", "is_active", "is_verified")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        ("Authentication", {"fields": ("email",)}),
        (
            "Permissions",
            {"fields": ("is_superuser", "is_staff", "is_active", "is_verified")},
        ),
        (
            "Group Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important_date", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "is_verified",
                ),
            },
        ),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
