# core/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "is_aluno", "is_professor", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("is_aluno", "is_professor")}),
    )

admin.site.register(Profile)
