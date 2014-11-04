from axh.media.scrapers.models import Movie
from axh.media.persist.models import MovieSummaryModel

__author__ = 'Alex Haslehurst'


class MediaFactory:
    @staticmethod
    def get_movie_summary_model(movie_summary):
        if not isinstance(movie_summary, Movie):
            raise TypeError("Expecting axh.media.scrapers.models.Movie")

        return MovieSummaryModel(media_source_id=movie_summary.media_source.value, title=movie_summary.title,
                                 year=movie_summary.year, image=movie_summary.image, imdb=movie_summary.imdb,
                                 rating=movie_summary.rating, trailer=movie_summary.trailer,
                                 synopsis=movie_summary.synopsis)

