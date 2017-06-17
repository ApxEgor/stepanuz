from django import forms
from django.contrib import admin
from movie.models import Movie, Seasons, Series



# class SeriesForm(forms.ModelForm):
#
#     class Meta:
#         model = Series
#         # movie = Movie.objects.filter(movie_name= ?)
#         # season_name = forms.ModelChoiceField(queryset=movie)
#         fields = ['movie', 'season_name' , 'series_name', 'url']

# class SeriesAdmin(admin.ModelAdmin):
#     form = SeriesForm

class SeriesInline(admin.StackedInline):
    model = Series


class SeasonsAdmin(admin.ModelAdmin):
    inlines = [
        SeriesInline,
    ]


class SeasonsInline(admin.StackedInline):
    model = Seasons


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        SeriesInline,
        SeasonsInline,
    ]



admin.site.register(Movie, MovieAdmin)
admin.site.register(Seasons, SeasonsAdmin)
admin.site.register(Series)


