from movie import Movie, Actor
from movie.view import View


def main():
    view = View()
    view.show_all()
    movie_to_add = Movie(
        title="The Imitation Game",
        date_released=2014,
        actors=[
            Actor(first_name="Benedict", last_name="Cumberbatch", role="Alan Turing"),
            Actor(first_name="Keira", last_name="Knightley", role="Joan Clarke")
        ]
    )
    view.add_movie(movie_obj=movie_to_add)
    view.show_all()


if __name__ == '__main__':
    main()
