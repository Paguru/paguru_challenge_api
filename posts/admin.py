from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content']


admin.site.register(Post, PostAdmin)
