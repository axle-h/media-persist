from axh.media.scrapers.models import MediaSource
from axh.media.persist.context import MediaContext
from axh.media.persist.factory import MediaFactory
from axh.media.persist.models import MediaSourceModel

__author__ = 'Alex Haslehurst'


class MovieRepository:
    def __init__(self, connection_string, echo_sql):
        self.db = MediaContext(connection_string, echo_sql)
        self.db.drop_and_create()

        # add default models
        media_sources = [MediaSourceModel(id=source.value, media_source=source.name) for source in MediaSource]
        session = self.db.SessionMaker()
        session.add_all(media_sources)
        session.commit()

    def add_movie(self, movie):
        session = self.db.SessionMaker()
        movie = MediaFactory.get_movie_summary_model(movie)
        session.add(movie)
        session.commit()





