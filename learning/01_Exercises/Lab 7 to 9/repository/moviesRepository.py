from repository.repository import repository


class moviesRepository(repository):
    def __init__(self):
        self.database = []
        self.rentedMovies = []
        self.currentID = 1
        self.currentAvailability = "Available"

    def save(self, movie):
        movie.id = self.currentID
        movie.availability = self.currentAvailability
        self.database.append(movie)
        self.currentID += 1

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

    def getMovie(self, theMovie):
        for movie in self.getAll():
            if theMovie == movie.title:
                return movie
