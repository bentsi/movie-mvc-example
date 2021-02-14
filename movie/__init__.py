class Actor:
    def __init__(self, first_name, last_name, role):
        self._first_name = first_name
        self._last_name = last_name
        self._role = role

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def role(self):
        return self._role

    def __str__(self):
        return f"{self.first_name} {self.last_name} as {self.role}"


class Movie:
    def __init__(self, title, date_released, actors):
        self._title = title
        self._date_released = date_released
        self._actors = actors

    @property
    def title(self):
        return self._title

    @property
    def date_released(self):
        return self._date_released

    @property
    def actors(self):
        return self._actors

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Release year: {self.date_released}\n" \
               f"Cast:\n  " + "\n  ".join(map(str, self.actors))
