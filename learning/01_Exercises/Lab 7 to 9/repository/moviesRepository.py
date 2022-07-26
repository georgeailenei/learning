from repository.repository import repository


class moviesRepository(repository):
    def __init__(self):
        self.movies = []
        self.currentID = 1

    def save(self, movie):
        # Save the movie given by the user and implement a unique ID.
        movie.id = self.currentID
        self.movies.append(movie)
        self.currentID += 1

    def saveAll(self, movies):
        # Save all the movies to the movieRepo.
        for movie in movies:
            self.save(movie)
        return self.movies

    def remove(self, ID):
        # Remove the desired movie by saving all the other movies in a new list.
        updateRepo = []
        for movie in self.movies:
            if movie.id != ID:
                updateRepo.append(movie)
        return updateRepo

    def removeAll(self):
        # Remove all the items from the list.
        return self.movies.clear()

    def getAll(self):
        # Get the list with the movies.
        return self.movies
