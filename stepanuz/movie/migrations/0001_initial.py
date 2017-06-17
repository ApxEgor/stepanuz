# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-10 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_content', models.CharField(choices=[('m', 'Фильм'), ('s', 'Сериал'), ('a', 'Аниме'), ('t', 'ТВ передачи')], max_length=255, verbose_name='Media content')),
                ('movie_name', models.CharField(max_length=255, verbose_name='Movie name')),
                ('release_date', models.DateField(verbose_name='Start_date')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('genre', models.CharField(choices=[('dr', 'Драма'), ('dt', 'Детектив'), ('kr', 'Криминал'), ('km', 'Комедия'), ('b', 'Боевик')], max_length=255, verbose_name='Movie genre')),
                ('aсtors', models.CharField(max_length=255, verbose_name='Actors')),
                ('description', models.TextField(verbose_name='Description')),
                ('movie_pic', models.ImageField(upload_to='', verbose_name='Movie picture')),
                ('url', models.URLField(verbose_name='Url video')),
            ],
        ),
    ]