from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

#ghjhgjk

RATING_Choices = {
    ('V', 'Verithanam - V'),
    ('T', 'Tharumaaruu - T'),
    ('M', 'Massu - M'),
    ('A', 'Attu - A'),
}

class Genre(models.Model):
    genres = models.CharField(max_length=39, unique=True)

def __str__(self):
    return "%s" % self.genres

class Country(models.Model):
    country = models.CharField(max_length=35, unique=True)

def __str__(self):
    return "%s" % self.country

class Stars(models.Model):
    stars = models.CharField(max_length=5, unique=True)

def __str__(self):
    return "%s" % self.stars

class Film(models.Model):
        Film_name = models.CharField(max_length=25, blank=False, unique=True)
        Year = models.IntegerField()
        Rating = models.CharField(max_length=80, choices=RATING_Choices, default="V")
        Duration = models.IntegerField()
        genres = models.ManyToManyField(Genre)
        Release_date = models.DateTimeField(auto_now=False)
        country = models.ManyToManyField(Country)
        User_rating =  models.DecimalField(max_digits=10, decimal_places=1, default=('0.0'))
        Display_Image = models.ImageField(upload_to="Disp/")
        Banner_Image = models.ImageField(upload_to="Banp/")
        Trailer = models.URLField(blank=True)
        Description = models.TextField()
        Director = models.CharField(max_length=80, blank=False)
        Writer = models.CharField(max_length=80, blank=False)
        stars = models.ManyToManyField(Stars)
        Metascore = models.IntegerField()
        User_Review = models.IntegerField()
        Critic_Review = models.IntegerField()
        Popularity = models.IntegerField()
        Created_Date = models.DateTimeField()
        Modified_Date =models.DateTimeField()
        CreatedBy = models.ForeignKey(User, null=True, blank=True)


def __str__(self):
    return "%s" % self.film_name
