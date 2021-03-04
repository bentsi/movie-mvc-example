class Controller:
    def __init__(self, model):
        self.model = model

    def add_movie(self, movie_obj):
        self.model.add_movie(movie_obj)