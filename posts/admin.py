"""Posts admin classes."""

#Django
from django.contrib import admin

#Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'created', 'modified')
    search_fields = ('title', 'user__username')
    list_filter = ('created', 'modified', 'user__is_active')

    fieldsets = (
        ('Post', {
            'fields': (
                ('photo', 'title'),
            )
        }),
    )
