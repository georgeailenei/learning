
class movie:
    def __init__(self, title, description, genre):
        self.id = None
        self.title = title
        self.description = description
        self.genre = genre
        self.availability = None

    def __str__(self):
        return f"{self.id} : {self.title} : {self.description} : {self.genre} : {self.availability}"

    def __repr__(self):
        return f"{self.id} : {self.title} : {self.description} : {self.genre} : {self.availability}"


class client:
    def __init__(self, name, CNP):
        self.id = None
        self.name = name
        self.CNP = CNP
        self.rentedMovies = ""

    def __str__(self):
        return f"{self.id} : {self.name} : {self.CNP} : {self.rentedMovies}"

    def __repr__(self):
        return f"{self.id} : {self.name} : {self.CNP} : {self.rentedMovies}"
