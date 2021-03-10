class Actor:
    def __init__(self, name, last_name, role):
        self.name = name
        self.last_name = last_name
        self.role = role

    def __str__(self):
        return f"name = {self.name}, last name = {self.last_name}, role in movie = {self.role}"


class Movie:
    def __init__(self, title, date_released, actors):
        self.title = title
        self.date_released = date_released
        self.actors = actors

    def __str__(self):
        list_of_str_actors = []
        for actor in self.actors:
            list_of_str_actors.append(str(actor))
        return f"title of movie = {self.title}, release date = {self.date_released}, actors = {list_of_str_actors}"
