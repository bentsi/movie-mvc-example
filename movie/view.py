from movie import Actor, Movie
from movie.controller import Conector


class View:

    def __init__(self):
        self.conector = Conector()

    def add_movie(self, movie_obj):
        self.conector.add_movie(movie_obj)

    def show_all(self):
        movies = self.conector.show_all()
        for movie in movies:
            print(movie)

    def dump(self):
        self.conector.dump()


if __name__ == '__main__':
    view = View()
    peter = [Actor(name="Peter", last_name="First", role="main")]
    movie_obj = Movie(title="Firs Peter", date_realized=2020, actor=peter)
