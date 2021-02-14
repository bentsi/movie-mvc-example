from movie.controller import Controller
from movie.model import Model


class View:

    def __init__(self):
        self.controller = Controller()
        self.model = Model()

    def show_all(self):
        movies = self.model.get_all_movies()
        for movie in movies:
            print(movie, end='\n\n')

    def add_movie(self, movie_obj):
        self.controller.add_movie(movie_obj)
