
class Movie:
    def __init__(self, title: str, description: str, genre: str):
        self.id = None
        self.title = title
        self.description = description
        self.genre = genre
        self.availability = None

    def __str__(self):
        return f"{self.id} : {self.title} : {self.description} : {self.genre} : {self.availability}"

    def __repr__(self):
        return f"{self.id} : {self.title} : {self.description} : {self.genre} : {self.availability}"


class Client:
    def __init__(self, name: str, CNP):
        self.id = None
        self.name = name
        self.CNP = CNP
        self.rented_movies = ""

    def __str__(self):
        return f"{self.id} : {self.name} : {self.CNP} : {self.rented_movies}"

    def __repr__(self):
        return f"{self.id} : {self.name} : {self.CNP} : {self.rented_movies}"
