from movie.model import Model


class Conector:
    def __init__(self):
        self.model = Model()

    def add_movie(self, movie_obj):
        self.model.add_movie(movie_obj)

    def show_all(self):
        return self.model.get_all_movie()

    def dump(self):
        self.model.dump_to_yml()