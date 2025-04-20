# KwentasApp/admin.py

from django.contrib import admin
from .models import CustomUser
from unfold.admin import ModelAdmin
from django.contrib import admin

from .models import UploadedFileData

class UploadedFileDataAdmin(ModelAdmin):
    list_display = ('file_id','file_name', 'file_type', 'project_code', 'uploaded_at')
    search_fields = ('file_name', 'file_type', 'project_code')
    list_filter = ('file_type',)

admin.site.register(UploadedFileData, UploadedFileDataAdmin)

class CustomUserAdmin(ModelAdmin):
    list_display = ('username', 'email', 'department', 'is_staff')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'department', 'name')}),  # Include 'name' here
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'department', 'name', 'password1', 'password2'),  # Include 'name' here
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
