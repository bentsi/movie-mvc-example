import json
from movie.movie_basic import Movie, Actor


class Model:
    def __init__(self):
        self._dump_filename = "movies.json"
        self._all_movies = []
        self.show_all()

    def get_all_movies(self):
        return self._all_movies

    def dump(self):
        movies_dicts_for_dump = [movie.__dict__ for movie in self._all_movies]
        for movie_dict in movies_dicts_for_dump:
            movie_dict["actors"] = [actor.__dict__ for actor in movie_dict["actors"]]
        with open(file=self._dump_filename, mode="w") as file:
            json.dump(movies_dicts_for_dump, file)
        print(f"All movies were dumped, there are {len(movies_dicts_for_dump)} "
              f"movies stored in '{self._dump_filename}'.\n")


    def show_all(self):
        """loads all movies from file"""
        print(f"We have:")
        with open(self._dump_filename, mode="r") as file:
            serialized_movie = json.load(file)
            for movie in serialized_movie:
                actors = [Actor(**actor) for actor in movie["actors"]]
                movie = Movie(title=movie["title"],
                              date_released=movie["date_released"],
                              actors=actors)
                print(f"{movie.__str__()}\n")


    def add_movie(self, movie_obj):
        self._all_movies.append(movie_obj)
        print(f"The following movie was added to the list \n{movie_obj.__str__()}\n")


if __name__ == "__main__":
    model = Model()
    movie_obj = Movie(
        title="The Imitation Game",
        date_released=2014,
        actors=[
            Actor(name="Benedict", last_name="Cumberbatch", role="Alan Turing"),
            Actor(name="Kira", last_name="Knightley", role="Joan Clarke")
        ]
    )

    movie_obj_2 = Movie(
        title="The Diamond Arm",
        date_released=1969,
        actors=[
            Actor(name="Yuri", last_name="Nikulin", role="Semyon Semyonovich Gorbunkov"),
            Actor(name="Andrey", last_name="Mironov", role="Gennadiy Kozodoyev, aka Gesha")
        ]
    )

    model.add_movie(movie_obj)
    model.add_movie(movie_obj_2)
    model.dump()
    model.show_all()