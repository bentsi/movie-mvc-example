class Actor:
    def __init__(self, name, last_name, role):
        self.name = name
        self.last_name = last_name
        self.role = role

    def __str__(self):
        return f"Actor: {self.name} {self.last_name}; role: {self.role}\n"


class Movie:
    def __init__(self, title, date_released, actors):
        self.title = title
        self.date_released = date_released
        self.actors = actors

    def __str__(self):
        return f"Movie title: {self.title}\n" \
               f"Data released: {self.date_released}\n" \
               f"Actors:\n{self.print_pretty_actors()}"
    def print_pretty_actors(self):
        actors_str = ""
        for actor in self.actors:
            actors_str += str(actor)
        return actors_str