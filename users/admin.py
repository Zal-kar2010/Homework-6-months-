from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from django.forms import ModelForm

class UserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    list_display = ("email", "first_name", "last_name", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal", {"fields": ("first_name", "last_name", "phone_number")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password", "password2", "is_staff", "is_superuser", "phone_number"),
        }),
    )

admin.site.register(CustomUser, UserAdmin)
