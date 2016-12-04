from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Film, Genre, Country, Stars
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Stars)
