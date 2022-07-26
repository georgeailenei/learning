class ControllerError(Exception):
    pass


class Controller:
    def __init__(self, moviesRepository, clientsRepository, validatorForMovie, validatorForClient):
        self.moviesRepository = moviesRepository
        self.clientsRepository = clientsRepository
        self.validatorForMovie = validatorForMovie
        self.validatorForClient = validatorForClient

    def addClient(self, Client):
        # Save the client's information in the list.
        if self.validatorForClient.validator(Client):
            self.clientsRepository.save(Client)
        else:
            print(f"The {Client}'s details appears to be wrong, please try again.")

    def removeMovie(self, ID):
        # Remove a movie by ID.
        # Notes for me. This method does not work properly. I cannot figure it out why...
        newMovieList = self.moviesRepository.remove(ID)
        self.moviesRepository.removeAll()
        self.moviesRepository.saveAll(newMovieList)

    def addMovie(self, movie):
        # Save the movie information in the list by validating the information given.
        if self.validatorForMovie.validator(movie):
            self.moviesRepository.save(movie)
        else:
            print(f"The {movie} contains some wrong information")

    def movieList(self):
        # Get all the movies from the list.
        return self.moviesRepository.getAll()

    def clientList(self):
        # Get all the clients from the list.
        return self.clientsRepository.getAll()
