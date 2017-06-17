from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django import forms
from movie.models import Movie, Seasons

class MovieListView(ListView):
	template_name = "movie/movie_list.html"
	model = Movie
	context_object_name = "movies"
	queryset = Movie.objects.filter(media_content='m')


class MovieDetailView(DetailView):
	template_name = "movie/movie_detail.html"
	model = Movie
	context_object_name = "movie"


class SerialsListView(ListView):
	template_name = "movie/serials_list.html"
	model = Movie
	context_object_name = "serials"
	queryset = Movie.objects.filter(media_content='s')


class SerialsDetailView(DetailView):
	template_name = "movie/serial_detail.html"
	model = Movie
	context_object_name = "serial"


class AnimeListView(ListView):
	template_name = "movie/anime_list.html"
	model = Movie
	context_object_name = "animes"
	queryset = Movie.objects.filter(media_content='a')


class AnimeDetailView(DetailView):
	template_name = "movie/anime_detail.html"
	model = Movie
	context_object_name = "anime"


class TVListView(ListView):
	template_name = "movie/tv_list.html"
	model = Movie
	context_object_name = "tvs"
	queryset = Movie.objects.filter(media_content='t')


class TVDetailView(DetailView):
	template_name = "movie/tv_detail.html"
	model = Movie
	context_object_name = "tv"


class TVSeasonSeriasView(ListView):
	template_name = "movie/tv_season_serias.html"
	model = Movie
	context_object_name = "tv"


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

