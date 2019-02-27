"""User admin classes."""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin."""
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_number')

    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
                )
        }),
        ('Extra Info', {
            'fields': (
                ('website'),
                ('phone_number'),
                ('biography')
            )
        }),
        ('Meta Data', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )

    readonly_fields = ('created', 'modified')

class ProfileInLine(admin.StackedInline):
    """Profile inline admin for users."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Adds profile admin to base user admin"""
    inlines = (ProfileInLine,)

    list_display = ('username', 'first_name', 'last_name', 'is_active', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)