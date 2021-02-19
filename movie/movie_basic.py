class Actor:
    def __init__(self, name, last_name, role):
        self.name = name
        self.last_name = last_name
        self.role = role

    def __str__(self):
        return f"{self.name} {self.last_name} as {self.role}"


class Movie:
    def __init__(self, title, date_released, actors):
        self.title = title
        self.date_released = date_released
        self.actors = actors

    def __str__(self):
        actors = ", ".join([str(name) for name in self.actors])
        return f"Movie - '{self.title}' ({self.date_released}). \nStarring with: {actors}"


if __name__ == "__main__":
    movie = Movie(
        title="The Imitation Game",
        date_released=2014,
        actors=[
            Actor(name="Benedict", last_name="Cumberbatch", role="Alan Turing"),
            Actor(name="Kira", last_name="Knightley", role="Joan Clarke")
        ]
    )
    print(movie)