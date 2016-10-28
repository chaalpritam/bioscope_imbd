from django.contrib import admin
from .models import Film, Genre, Country, Stars
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ("film_name", "created_date")
    prepopulated_fields = {"slug": ("film_name",)}


admin.site.register(Film, FilmAdmin)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Stars)
