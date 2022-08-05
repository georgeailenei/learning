from repository.repository import repository


class moviesRepository(repository):
    def __init__(self):
        self.database = []
        self.currentID = 1
        self.currentCount = 0
        self.currentAvailability = "Available"
        self.trackRentedMovies = {}

    def save(self, movie):
        movie.id = self.currentID
        movie.availability = self.currentAvailability
        self.database.append(movie)
        self.trackRentedMovies[movie.title] = self.currentCount
        self.currentID += 1

    def addCount(self, movie):
        self.trackRentedMovies[movie] += 1

    def update(self, ID, newMovie):
        updatedDatabase = []
        for movie in self.database:
            if ID == str(movie.id):
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

    def get(self):
        pass
