# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    MEDIA_CHOICE = (('m', u'Фильм'),
                    ('s', u'Сериал'),
                    ('a', u'Аниме'),
                    ('t', u'ТВ передачи'))
    GENRE_CHOICE = (('dr', u'Драма'),
                    ('dt', u'Детектив'),
                    ('kr', u'Криминал'),
                    ('km', u'Комедия'),
                    ('b', u'Боевик'))

    media_content = models.CharField(max_length=255, choices=MEDIA_CHOICE, verbose_name=_('Media content'))
    movie_name = models.CharField(max_length=255, verbose_name=_('Movie name'))
    release_date = models.DateField(verbose_name=_('Release date'))
    country = models.CharField(max_length=255, verbose_name=_('Country'))
    genre = models.CharField(max_length=255, choices=GENRE_CHOICE, verbose_name=_('Movie genre'))
    actors = models.CharField(max_length=255, verbose_name=_('Actors'))
    description = models.TextField(verbose_name=_('Description'))
    movie_pic = models.ImageField(verbose_name=_('Movie picture'))
    url = models.URLField(max_length=200, verbose_name=_('Url video'))

    def __str__(self):
        return "%s" % (self.movie_name)


class Seasons(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    season_name = models.CharField(max_length=255, verbose_name=_('Season name'))

    def __str__(self):
        return "%s (%s)" % (self.movie, self.season_name)


class Series(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    season_name = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    series_name = models.CharField(max_length=50, verbose_name=_('Series name'))
    url = models.URLField(max_length=200, verbose_name=_('Url video'))

    def __str__(self):
        return "%s (%s) - %s" % (self.movie, self.season_name, self.series_name)