from repository.repository import repository


class moviesRepository(repository):
    def __init__(self):
        self.database = []
        self.currentID = 1

    def save(self, movie):
        # Save the movie given by the user and implement a unique ID.
        movie.id = self.currentID
        self.database.append(movie)
        self.currentID += 1

    def saveAll(self, movies):
        # Save all the movies to the movieRepo.
        self.currentID = 1
        for movie in movies:
            self.save(movie)
        return self.database

    def remove(self, ID):
        # Remove the desired movie by saving all the other movies in a new list.
        updateRepo = [movie for movie in self.database if ID not in movie.__repr__()]
        return updateRepo

    def removeAll(self):
        # Remove all the items from the list.
        return self.database.clear()

    def getAll(self):
        # Get the list with the movies.
        return self.database

    def getID(self):
        idList = [movie.id.__repr__() for movie in self.database]
        return idList

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
