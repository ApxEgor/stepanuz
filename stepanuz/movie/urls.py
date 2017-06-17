from django.conf.urls import url

from movie.views import MovieListView, MovieDetailView, SerialsListView, SerialsDetailView, AnimeListView, AnimeDetailView, TVListView, TVDetailView, TVSeasonSeriasView


urlpatterns = [
	url(r'^movie/(?P<pk>\d+)/$', MovieDetailView.as_view(), name="movie-detail"),
	url(r'^movies/$', MovieListView.as_view(), name='movies-list'),
    url(r'^serial/(?P<pk>\d+)/$', SerialsDetailView.as_view(), name="serial-detail"),
	url(r'^serials/$', SerialsListView.as_view(), name='serials-list'),
    url(r'^anime/(?P<pk>\d+)/$', AnimeDetailView.as_view(), name="anime-detail"),
	url(r'^anime/$', AnimeListView.as_view(), name='anime-list'),
    url(r'^tv/(?P<pk>\d+)/$', TVDetailView.as_view(), name="tv-detail"),
	url(r'^tv/season/(?P<pk>\d+)/$', TVSeasonSeriasView.as_view(), name="tv-serias"),
	url(r'^tv/$', TVListView.as_view(), name='tv-list'),
	]
