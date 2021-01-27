class Model:
    def __init__(self):
        self._dump_filename = "./movies.dump"
        self._all_movies = []
        self.load()

    def get_all_movies(self):
        return self._all_movies

    def dump(self, movie_obj):
        pass

    def load(self):
        """loads all movies from file"""
        pass

    def add_movie(self, movie_obj):
        self._all_movies.append(movie_obj)
        self.dump(movie_obj)
