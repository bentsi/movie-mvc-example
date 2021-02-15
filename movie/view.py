from movie.controller import Controller


class View:

    def __init__(self):
        self.controller = Controller()

    def show_all(self):
        movies = self.controller.get_all_movies()
        for movie in movies:
            print(movie)

    def add_movie(self, movie_obj):
        self.controller.add_movie(movie_obj)
