import pickle


class Model:
    def __init__(self):
        self._dump_filename = "./movies.dump"
        self._all_movies = []
        self._all_file_name = []

    def get_all_movies(self):
        return self._all_movies

    def dump(self, movie_obj):
        file_name = f"movies/{movie_obj.title}_{movie_obj.date_released}.pickle"
        file = open(file_name, "wb")
        pickle.dump(movie_obj, file)
        file.close()
        self._all_file_name.append(file_name)

    def load(self):
        all_load_movies = []
        for name in self._all_file_name:
            file = open(name, "rb")
            movie_from_file = pickle.load(file)
            file.close()
            all_load_movies.append(movie_from_file)
        return all_load_movies

    def add_movie(self, movie_obj):
        self._all_movies.append(movie_obj)
        self.dump(movie_obj)
