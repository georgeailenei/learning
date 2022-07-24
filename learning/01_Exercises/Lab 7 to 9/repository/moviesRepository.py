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

    def remove(self):
        pass

    def getAll(self):
        # Get the list with the movies.
        return self.movies
