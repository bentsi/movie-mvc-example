from movie.model import Model


class Controller:
    def __init__(self):
        self.model = Model()

    def add_movie(self, movie_obj):
        self.model.add_movie(movie_obj)

    def get_all_movies(self):
        self.model.get_all_movies()
