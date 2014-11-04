from axh.media.scrapers import scrape_movies
from axh.media.scrapers.models import Movie, MediaSource
import axh.media.persist

__author__ = 'alexanderh'

movie = Movie(MediaSource.Yts, 'title', 2014, 'link', 'torrent', 'magnet', 'imdb', 3.4, 'genre', '1080p',
              300, 400, 'synopsis', 'image', 'trailer')

repository = axh.media.persist.create_default_movie_repository()
repository.add_movie(movie)