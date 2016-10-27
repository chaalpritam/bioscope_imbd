# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 18:08
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('film_name', models.CharField(max_length=80, unique=True)),
                ('year', models.IntegerField()),
                ('rating', models.CharField(choices=[('G', 'General Audiences - G'), ('PG', 'Parental Guidance Suggested - PG'), ('PG-13', 'Parents Strongly Cautioned - PG -13 '), ('R', 'Restricted - R'), ('NC-17', 'Adults Only - NC-17')], default='G', max_length=80)),
                ('hours_min', models.IntegerField()),
                ('release_date', models.DateTimeField()),
                ('user_rating', models.DecimalField(decimal_places=1, default=Decimal('0.0'), max_digits=10)),
                ('display_image', models.ImageField(upload_to='display_picture/')),
                ('banner_image', models.ImageField(upload_to='banner_picture/')),
                ('trailer_link', models.URLField(blank=True, help_text='Trailer url')),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=80)),
                ('writer', models.CharField(max_length=80)),
                ('metascore', models.IntegerField()),
                ('user_review', models.IntegerField()),
                ('critic_review', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('slug', models.SlugField(max_length=80, unique=True)),
                ('country', models.ManyToManyField(to='films.Country')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(to='films.Genre'),
        ),
        migrations.AddField(
            model_name='film',
            name='stars',
            field=models.ManyToManyField(to='films.Stars'),
        ),
    ]
