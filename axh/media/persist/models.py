from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, Float, Text, UniqueConstraint, Index
from axh.media.persist.context import MediaContext

__author__ = 'Alex Haslehurst'


class MediaSourceModel(MediaContext.Base):
    __tablename__ = 'media_source'
    id = Column(Integer(), primary_key=True, nullable=False)
    media_source = Column(String(16), nullable=False)


class MovieSummaryModel(MediaContext.Base):
    __tablename__ = 'movies'
    __table_args__ = (UniqueConstraint('title', 'year', name='UniqueConstraint_title_year'),
                      Index('Index_title_year', 'title', 'year', unique=True),
                      Index('Index_imdb', 'imdb', unique=True),
                      Index('Index_rating', 'rating'))

    id = Column(Integer(), primary_key=True, nullable=False)
    media_source_id = Column(Integer(), ForeignKey(MediaSourceModel.__tablename__ + '.' + MediaSourceModel.id.name),
                             nullable=False)
    title = Column(String(128), nullable=False)
    year = Column(Integer(), nullable=False)
    image = Column(String(128), nullable=False)
    imdb = Column(String(16), nullable=False)
    rating = Column(Float(asdecimal=True), nullable=False)
    trailer = Column(String(128), nullable=False)
    synopsis = Column(Text(), nullable=False)

