from movie import Movie, Actor
from movie.view import View


def main():
    view = View()
    print("------------No movies added---------------")
    view.show_all()
    print("------------Adding 1st movie-------------")
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
    print("------------Adding 2nd movie-------------")
    movie_to_add = Movie(
        title="A Beautiful Mind",
        date_released=2001,
        actors=[
            Actor(first_name="Russell", last_name="Crowe", role="John Nash"),
            Actor(first_name="Ed", last_name="Harris", role="William Parcher"),
            Actor(first_name="Jennifer", last_name="Connelly", role="Alicia Nash")
        ]
    )
    view.add_movie(movie_obj=movie_to_add)
    view.show_all()


if __name__ == '__main__':
    main()
