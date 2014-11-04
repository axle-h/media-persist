import json
import os
from axh.media.persist.repository import MovieRepository

__author__ = 'Alex Haslehurst'


def create_default_movie_repository():
    # Read config
    config_path = os.path.realpath('./config.json')
    config_file = open(config_path)
    config_json = json.load(config_file)
    config_file.close()

    return MovieRepository(config_json['connection_string'], config_json['echo_sql'])



