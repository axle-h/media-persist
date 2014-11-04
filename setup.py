from distutils.core import setup

__author__ = 'Alex Haslehurst'

setup(
    name='media_persist',
    version='0.1',
    packages=['axh', 'axh.media', 'axh.media.persist'],
    namespace_packages=['axh', 'axh.media'],
    url='https://github.com/axle-h/media-persist',
    license='',
    author='Alex Haslehurst',
    author_email='alex.haslehurst@gmail.com',
    description='Repository layer for media-scrapers',
    requires=['media_scrapers', 'sqlalchemy'],
    install_requires=['media_scrapers', 'sqlalchemy']
)
