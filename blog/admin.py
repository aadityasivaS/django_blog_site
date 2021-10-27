from django.contrib import admin
from .models import Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_filter = ('status',)
    list_display = ('title', 'author', 'status', 'created_on')
    pass
