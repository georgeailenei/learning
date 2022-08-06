import itertools


class ControllerError(Exception):
    pass


class Controller:
    def __init__(self, moviesRepository, clientsRepository, validatorForMovie, validatorForClient):
        self.moviesRepository = moviesRepository
        self.clientsRepository = clientsRepository
        self.validatorForMovie = validatorForMovie
        self.validatorForClient = validatorForClient

    # ADD SECTION
    def addMovie(self, movie):
        # Save the movie information in the list by validating the information given.
        if self.validatorForMovie.validator(movie, self.moviesRepository.getNames()):
            self.moviesRepository.save(movie)
            print(f"\n{movie} has been added to the list.")
        else:
            print(f"The {movie} contains some wrong information")

    def addClient(self, Client):
        # Save the client's information in the list.
        if self.validatorForClient.validator(Client, self.clientsRepository.getNames()):
            self.clientsRepository.save(Client)
            print(f"\n{Client} has been added to the list.")
        else:
            print(f"The {Client}'s details appears to be wrong, please try again.")

    # REMOVE SECTION
    def removeMovie(self, ID):
        if ID in self.moviesRepository.getIdList():
            newMovieList = self.moviesRepository.remove(ID)
            self.moviesRepository.removeAll(), self.moviesRepository.saveAll(newMovieList)
            print(f"\nThe movie with {ID} id has been removed.")
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    def removeClient(self, ID):
        if ID in self.clientsRepository.getIdList():
            newClientList = self.clientsRepository.remove(ID)
            self.clientsRepository.removeAll(), self.clientsRepository.saveAll(newClientList)
            print(f"\nThe client with {ID} id has been removed.")
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    # UPDATE SECTION
    def updateMovie(self, ID, newMovie):
        if self.validatorForMovie.checkID(ID, self.moviesRepository.getIdList()):
            self.moviesRepository.update(ID, newMovie)
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    def updateClient(self, ID, newClient):
        if self.validatorForMovie.checkID(ID, self.clientsRepository.getIdList()):
            self.clientsRepository.update(ID, newClient)
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    # SEARCH SECTION
    def searchMovies(self, findMovie):
        if findMovie in self.moviesRepository.getNames():
            for movie in self.moviesRepository.getAll():
                if movie.title == findMovie:
                    print(f"{findMovie} | Found! | Full information: ")
                    print(f"{movie}")
        else:
            print(f"{findMovie} | Could not been found! Please try again.")

    def searchClients(self, findClient):
        if findClient in self.clientsRepository.getNames():
            for client in self.clientsRepository.getAll():
                if client.name == findClient:
                    print(f"{findClient} | Found! | Full information: ")
                    print(f"{client}")
        else:
            print(f"{findClient} | Could not been found! Please try again.")

    # RENT SECTION
    def rentMovies(self, theClient, theMovie):
        if theClient in self.clientsRepository.getNames():
            if theMovie in self.moviesRepository.getNames():
                if self.validatorForMovie.checkAvailability(self.moviesRepository.getMovie(theMovie).availability):
                    self.clientsRepository.saveMovie(theClient, self.moviesRepository.getMovie(theMovie).title)
                    self.moviesRepository.updateStatus(self.moviesRepository.getMovie(theMovie))
                    self.moviesRepository.addCount(theMovie), self.clientsRepository.addCount(theClient)
                else:
                    print(f"\n{theMovie} is not available")
            else:
                print(f"\nWe do not have {theMovie} in our store.")
        else:
            print(f"\n{theClient} is not in the client list.")

    # RETURN SECTION
    def returnMovies(self, theClient, theMovie):
        if theClient in self.clientsRepository.getNames():
            if theMovie in self.moviesRepository.getNames():
                if theMovie in self.clientsRepository.getClient(theClient).rentedMovies:
                    self.clientsRepository.removeMovie(self.moviesRepository.getMovie(theMovie).title)
                    self.moviesRepository.updateStatus(self.moviesRepository.getMovie(theMovie))
                    print(f"\nThank Mr.{theClient} for returning the movie: {theMovie}")
                else:
                    print(f"\n{theMovie} is not rented by {theClient}")
            else:
                print(f"\nWe do not have {theMovie} in our store.")
        else:
            print(f"\n{theClient} is not in the client list.")

    # REPORT SECTION
    # DISPLAY THE CLIENTS THAT HAVE MOVIES IN ALPHABETICAL ORDER
    def displayClientsInOrder(self):
        clientsWithMovies = []
        for client in self.clientsRepository.getAll():
            if self.validatorForClient.moviesRented(client):
                clientsWithMovies.append(client.name)

        clients = sorted(clientsWithMovies)
        if len(clientsWithMovies) == 0:
            print("NONE OF THE MOVIES ARE RENTED")
        else:
            for client in clients:
                print(client + " has " + str(self.clientsRepository.getMovieCount(client)) + " movie/s")

    # DISPLAY THE MOST RENTED MOVIE
    def displayMostRentedMovies(self):
        values = [count for movie, count in self.moviesRepository.trackRentedMovies.items()]
        if max(values, default=0) != 0:
            for movie, count in self.moviesRepository.trackRentedMovies.items():
                if count == max(values):
                    print(movie)
        else:
            print("NONE OF THE MOVIES")

    # DISPLAY TOP 30% CLIENTS
    def displayClientsWithMostMovies(self):
        values = [count for count in self.clientsRepository.trackClientRentedMovies.values()]
        keys = [name for name in self.clientsRepository.trackClientRentedMovies.keys()]
        clients = self.clientsRepository.trackClientRentedMovies
        values.sort(), values.reverse()

        clientsInOrder = {}
        check = 0
        valueChecker = 0

        while len(values) > check:
            if values[check] == clients[keys[valueChecker]]:
                clientsInOrder[keys[valueChecker]] = values[check]
                check += 1
                valueChecker = 0
            else:
                valueChecker += 1

        x = (len(clientsInOrder) * 30) / 100
        top30 = dict(itertools.islice(clientsInOrder.items(), round(x)))

        if len(top30) == 0:
            print("NONE OF THE CLIENTS")

        return top30
