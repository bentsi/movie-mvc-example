import json
from os import path
from movie import Actor, Movie


class Model:
    def __init__(self):
        self._dump_filename = "./movies.json"
        self._all_movies = []

    @property
    def all_movies(self):
        return self._all_movies

    @all_movies.setter
    def all_movies(self, value):
        self._all_movies = value

    def get_all_movies(self):
        return self.load()

    def dump(self, movie_obj):
        with open(self._dump_filename, "a") as file:
            json.dump(movie_obj.__dict__, file, default=lambda x: x.__dict__)
            file.write("\n")
        return

    def load(self):
        json_movies = []
        self.all_movies = []
        file_exists = path.isfile(self._dump_filename)
        if file_exists:
            with open(self._dump_filename) as file:
                for line in file:
                    movie_dict = json.loads(line)
                    json_movies.append(movie_dict)
            for movie in json_movies:
                actors = []
                for actor in movie["_actors"]:
                    actors.append(Actor(first_name=actor["_first_name"],
                                        last_name=actor["_last_name"],
                                        role=actor["_role"]))
                self.all_movies.append(Movie(title=movie["_title"],
                                             date_released=movie["_date_released"],
                                             actors=actors))
        return self.all_movies

    def add_movie(self, movie_obj):
        self.all_movies.append(movie_obj)
        self.dump(movie_obj)
