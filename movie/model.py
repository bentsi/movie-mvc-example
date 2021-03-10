import yaml


class Model:

    def __init__(self):
        # self._dump_filename = "./movies.dump"
        self._dump_filename = "movie_list.yaml"
        self._all_movies = []

    def get_all_movies(self):
        return self._all_movies

    def dump(self):
        with open(self._dump_filename, "w") as file:
            movie_dicts = []
            for movie in self._all_movies:
                movie_dicts.append(movie.__dict__)
            list_of_actors = []
            for movie_dict in movie_dicts:
                for actor in movie_dict["actors"]:
                    list_of_actors.append(actor.__dict__)
                movie_dict["actors"] = list_of_actors
            yaml.dump(movie_dicts, file)

    def load(self):
        """loads all movies from file"""
        with open(self._dump_filename, "r") as file:
            return yaml.safe_load(file)

    def add_movie(self, movie_obj):
        self._all_movies.append(movie_obj)
        self.dump()
        print(self.load())


