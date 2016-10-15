from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Create your models here.
RATING_CHOICES = (
('G', 'General Audiences - G'),
('PG', 'Parental Guidance Suggested - PG'),
('PG-13', 'Parents Strongly Cautioned - PG-13'),
('R', 'Restricted - R'),
('NC-17', 'Adults Only - NC-17'),
)

class Genre(models.Model):
    genres = models.CharField(max_length=30, unique=True)

    def __str__(self):
         return "%s" % self.Genre

class country(models.Model):
    country = models.CharField(max_length=60, unique=True)

    def __str__(self):
         return "%s" % self.country

class stars(models.Model):
    stars = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return "%s" % self.stars

class flim(models.Model):

     created_date = models.DateTimeField(auto_now_add=True)
     modified_date = models.DateTimeField(auto_now=True)
     film_name = models.CharField(max_length=20, blank=False, unique=True)
     year = models.IntegerField()
     rating = models.CharField(max_length=80, choices=RATING_CHOICES, default="G")
     hours_min = models.IntegerField()
     genres = models.ManyToManyField(Genre)
     release_date = models.DateTimeField(auto_now=False)
     country = models.ManyToManyField(country)
     user_rating = models.DecimalField(max_digits=10, decimal_places=1, default=Decimal('0.0'))
     display_image = models.ImageField(upload_to="display_picture/")
     banner_image = models.ImageField(upload_to="banner_picture/")
     trailer_link = models.URLField(blank=True, help_text="Trailer url")
     description = models.TextField()
     director = models.CharField(max_length=80, blank=False)
     writer = models.CharField(max_length=80, blank=False)
     stars = models.ManyToManyField(stars)
     metascore = models.IntegerField()
     user_review = models.IntegerField()
     critic_review = models.IntegerField()
     popularity = models.IntegerField()
     created_by = models.ForeignKey(User, null=True, blank=True)

     def __str__(self):
         return "%s" % self.flim_name
