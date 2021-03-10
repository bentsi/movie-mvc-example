from movie.controller import Controller
from movie.model import Model


class View:
    def __init__(self):
        self.model = Model()
        self.controller = Controller(model=self.model)

    def show_all(self):
        movies = self.model.get_all_movies()
        for movie in movies:
            print(movie)

    def add_movie(self, movie_obj):
        self.controller.add_movie(movie_obj)

