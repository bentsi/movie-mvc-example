import json


class Actor:
    def __init__(self, name: str, last_name: str, role: str):
        self.name = name
        self.last_name = last_name
        self.role = role

    def __str__(self):
        return f"{self.name.capitalize()} {self.last_name.capitalize()} ({self.role})"


class Movie:
    NEWLINE = '\n'

    def __init__(self, title: str, date_released: str, actors: list[Actor]):
        self.title = title
        self.release_date = date_released
        self.actors = actors

    def __str__(self):
        return f"{self.title.capitalize()} ({self.release_date}) Starring:\n{self.NEWLINE.join([str(a) for a in self.actors])}"
