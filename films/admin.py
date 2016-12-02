from django.contrib import admin
from .models import Film, Genre, Country, Stars
# Register your models here.
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Stars)
