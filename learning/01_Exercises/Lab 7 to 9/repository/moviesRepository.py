from repository.repository import repository


class moviesRepository(repository):
    def __init__(self):
        self.movies = []
        self.currentID = 1

    def save(self, movie):
        movie.id = self.currentID
        self.movies.append(movie)
        self.currentID += 1

    def remove(self):
        pass

    def getAll(self):
        return self.movies
