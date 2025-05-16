from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'resume', 'genres', 'created_at')
    search_fields = ('title',)
    list_filter = ('actors', 'genres',)
    ordering = ('-created_at',)
    list_per_page = 20
