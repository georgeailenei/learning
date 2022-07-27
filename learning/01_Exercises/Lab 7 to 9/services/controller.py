class ControllerError(Exception):
    pass


class Controller:
    def __init__(self, moviesRepository, clientsRepository, validatorForMovie, validatorForClient):
        self.moviesRepository = moviesRepository
        self.clientsRepository = clientsRepository
        self.validatorForMovie = validatorForMovie
        self.validatorForClient = validatorForClient

    # GET ID LIST
    def idList(self):
        return self.moviesRepository.getID()

    # DISPLAY LISTS - movies & clients.
    def movieList(self):
        # Get all the movies from the list.
        return self.moviesRepository.getAll()

    def clientList(self):
        # Get all the clients from the list.
        return self.clientsRepository.getAll()

    # ADD SECTION - add movies & clients.
    def addMovie(self, movie):
        # Save the movie information in the list by validating the information given.
        if self.validatorForMovie.validator(movie):
            self.moviesRepository.save(movie)
            print(f"\n{movie} has been added to the list.")
        else:
            print(f"The {movie} contains some wrong information")

    def addClient(self, Client):
        # Save the client's information in the list.
        if self.validatorForClient.validator(Client):
            self.clientsRepository.save(Client)
            print(f"\n{Client} has been added to the list.")
        else:
            print(f"The {Client}'s details appears to be wrong, please try again.")

    # REMOVE SECTION - remove movies & clients.
    def removeMovie(self, ID):
        # Remove a movie by ID.
        idList = self.moviesRepository.getID()

        if ID in idList:
            newMovieList = self.moviesRepository.remove(ID)
            self.moviesRepository.removeAll()
            self.moviesRepository.saveAll(newMovieList)
            print(f"\nThe movie with {ID} id has been removed.")
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    def removeClient(self, ID):
        # Remove a client by ID.
        if ID in self.idList():
            newClientList = self.clientsRepository.remove(ID)
            self.clientsRepository.removeAll()
            self.clientsRepository.saveAll(newClientList)
            print(f"\nThe client with {ID} id has been removed.")
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    # UPDATE Section - update movies & clients.
    def updateMovie(self, ID, newMovie):
        if self.validatorForMovie.checkID(ID, self.idList()):
            self.moviesRepository.update(ID, newMovie)
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")
