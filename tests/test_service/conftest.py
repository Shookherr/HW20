import pytest
from unittest.mock import MagicMock

from setup_db import db

from dao.model.movie import Movie
from dao.model.director import Director
from dao.model.genre import Genre

from dao.movie import MovieDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    director_01 = Director(id=1, name="Dir01")
    director_02 = Director(id=2, name="Dir02")
    director_03 = Director(id=3, name="Dir03")

    directors = {1: director_01, 2: director_02, 3: director_03}

    director_dao.get_one = MagicMock(return_value=director_01)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=director_01)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    genre_01 = Genre(id=1, name="Gen01")
    genre_02 = Genre(id=2, name="Gen02")
    genre_03 = Genre(id=3, name="Gen03")
    genre_04 = Genre(id=3, name="Gen04")

    genres = {1: genre_01, 2: genre_02, 3: genre_03, 4: genre_04}

    genre_dao.get_one = MagicMock(return_value=genre_01)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=genre_01)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)
    
    movie_01 = Movie(id=1, title="Film01", description="Descr01",  trailer="trail01",
                     year=2001, rating=1.0, genre_id=1, director_id=1)
    movie_02 = Movie(id=2, title="Film02", description="Descr02",  trailer="trail02",
                     year=2002, rating=2.0, genre_id=2, director_id=2)
    movie_03 = Movie(id=3, title="Film03", description="Descr03",  trailer="trail03",
                     year=2003, rating=3.0, genre_id=3, director_id=3)
    movie_04 = Movie(id=4, title="Film04", description="Descr04",  trailer="trail04",
                     year=2004, rating=4.0, genre_id=4, director_id=1)
    movie_05 = Movie(id=5, title="Film05", description="Descr05",  trailer="trail05",
                     year=2005, rating=5.0, genre_id=1, director_id=2)

    movies = {1: movie_01, 2: movie_02, 3: movie_03, 4: movie_04, 5: movie_05}

    movie_dao.get_one = MagicMock(return_value=movie_01)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=movie_01)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
