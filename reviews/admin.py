from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'comment', 'created_at')
    search_fields = ('movie',)
    list_filter = ('stars', 'created_at')
    ordering = ('-created_at',)
