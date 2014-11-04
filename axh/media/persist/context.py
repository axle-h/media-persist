from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlite3 import Connection as SQLite3Connection

__author__ = 'Alex Haslehurst'


class MediaContext:
    Base = declarative_base()

    def __init__(self, connection_string, echo=False):
        self._Engine = create_engine(connection_string, echo=echo)
        event.listen(self._Engine, 'connect', MediaContext._set_sqlite_pragma)
        self.SessionMaker = sessionmaker(bind=self._Engine)

    def drop_and_create(self):
        meta = self.Base.metadata
        meta.drop_all(self._Engine)
        meta.create_all(self._Engine)

    # Check we are using sqlite3 on connect and if so, enable foreign keys.
    @staticmethod
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        if isinstance(dbapi_connection, SQLite3Connection):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON;")
            cursor.close()