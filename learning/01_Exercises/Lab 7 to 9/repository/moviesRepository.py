from repository.repository import repository


class moviesRepository(repository):
    def __init__(self):
        self.database = []
        self.currentID = 1

    def update(self, ID, newMovie):
        updatedDatabase = []
        for movie in self.database:
            if ID in movie.__repr__():
                movie.title = newMovie.title
                movie.description = newMovie.description
                movie.genre = newMovie.genre
                updatedDatabase.append(movie)
            else:
                updatedDatabase.append(movie)
        self.removeAll(), self.saveAll(updatedDatabase)

    def getNames(self):
        nameList = [movie.title for movie in self.database]
        return nameList
