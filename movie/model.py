import json
from movie import Actor, Movie

class Model:
    def __init__(self):
        self._dump_filename = "./movies.json"
        self._all_movies = []
        self.load_all()

    def get_all_movies(self):
        return self._all_movies

    def dump_all(self):
        with open(self._dump_filename, "wt") as f:
            movie_dicts = [dict(movie.__dict__) for movie in self._all_movies]
            for movie_dict in movie_dicts:
                movie_dict["actors"] = [actor.__dict__ for actor in movie_dict["actors"]]
            json.dump(movie_dicts, f)

    def load_all(self):
        with open(self._dump_filename, "rt") as f:
            movies_serialized = json.load(f)
            for movie_dict in movies_serialized:
                actors = [Actor(**actor) for actor in movie_dict["actors"]]
                movie = Movie(movie_dict["title"], movie_dict["release_date"], actors)
                self._all_movies.append(movie)

    def add_movie(self, movie_obj):
        self._all_movies.append(movie_obj)
        self.dump_all()
