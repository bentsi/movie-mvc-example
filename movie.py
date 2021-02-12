from movie import Movie, Actor
from movie.view import View


def main():
    view = View()
    view.show_all()
    actors = [
        Actor(name="Peter", last_name="First", role="main_Hero"),
        Actor(name="Kira", last_name="Knightley", role="Joan Clarke"),
        Actor(name="Benedict", last_name="Cumberbatch", role="Alan Turing")
    ]
    movie_obj = Movie(title="Firs Peter", date_realized=2020, actor=actors)
    view.add_movie(movie_obj=movie_obj)
    view.dump()


if __name__ == '__main__':
    main()