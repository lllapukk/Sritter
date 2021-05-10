from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'header', 'text', 'author', 'published_date', 'image')


admin.site.register(Post, PostAdmin)
