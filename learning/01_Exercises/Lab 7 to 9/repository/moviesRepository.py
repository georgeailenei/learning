from repository.repository import repository


class moviesRepository(repository):
    def __init__(self):
        self.movies = []
        self.currentID = 1

    def save(self, movie):
        self.movies.append(movie)
        return self.movies

    def remove(self):
        pass

    def getAll(self):
        return self.movies
