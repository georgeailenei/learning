import itertools


class ControllerError(Exception):
    pass


class Controller:
    def __init__(self, moviesRepository, clientsRepository, validatorForMovie, validatorForClient):
        self.moviesRepository = moviesRepository
        self.clientsRepository = clientsRepository
        self.validatorForMovie = validatorForMovie
        self.validatorForClient = validatorForClient

    # CLEAN THIS CODE IS USELESS
    # GET MOVIE & CLIENT'S ID LIST
    def movieIDList(self):
        return self.moviesRepository.getID()

    def clientIDList(self):
        return self.clientsRepository.getID()

    # GET MOVIE & CLIENT'S NAME LIST
    def movieNameList(self):
        return self.moviesRepository.getNames()

    def clientNameList(self):
        return self.clientsRepository.getNames()

    # DISPLAY LISTS - movies & clients.
    def movieList(self):
        # Get all the movies from the list.
        return self.moviesRepository.getAll()

    def clientList(self):
        # Get all the clients from the list.
        return self.clientsRepository.getAll()
    # CLEAN THIS CODE IS USELESS

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
        if ID in self.movieIDList():
            newMovieList = self.moviesRepository.remove(ID)
            self.moviesRepository.removeAll()
            self.moviesRepository.saveAll(newMovieList)
            print(f"\nThe movie with {ID} id has been removed.")
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    def removeClient(self, ID):
        # Remove a client by ID.
        if ID in self.clientIDList():
            newClientList = self.clientsRepository.remove(ID)
            self.clientsRepository.removeAll()
            self.clientsRepository.saveAll(newClientList)
            print(f"\nThe client with {ID} id has been removed.")
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    # UPDATE SECTION - update movies & clients.
    def updateMovie(self, ID, newMovie):
        if self.validatorForMovie.checkID(ID, self.movieIDList()):
            self.moviesRepository.update(ID, newMovie)
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    def updateClient(self, ID, newClient):
        if self.validatorForMovie.checkID(ID, self.clientIDList()):
            self.clientsRepository.update(ID, newClient)
        else:
            print(f"\nThe ID: {ID} is invalid! Please try again.")

    # SEARCH SECTION - update movies & clients.
    def searchMovies(self, findMovie):
        if findMovie in self.movieNameList():
            for movie in self.movieList():
                if movie.title == findMovie:
                    print(f"{findMovie} | Found! | Full information: ")
                    print(f"{movie}")
        else:
            print(f"{findMovie} | Could not been found! Please try again.")

    def searchClients(self, findClient):
        if findClient in self.clientNameList():
            for client in self.clientList():
                if client.name == findClient:
                    print(f"{findClient} | Found! | Full information: ")
                    print(f"{client}")
        else:
            print(f"{findClient} | Could not been found! Please try again.")

    # RENT SECTION - Where clients can rent movies.
    def rentMovies(self, theClient, theMovie):
        if theClient in self.clientNameList():
            if theMovie in self.movieNameList():
                if self.validatorForMovie.checkAvailability(self.moviesRepository.getMovie(theMovie).availability):
                    self.clientsRepository.saveMovie(theClient, self.moviesRepository.getMovie(theMovie).title)
                    self.moviesRepository.getMovie(theMovie).availability = "NOT AVAILABLE"
                    self.moviesRepository.addCount(theMovie)
                    self.clientsRepository.addCount(theClient)
                else:
                    print(f"\n{theMovie} is not available")
            else:
                print(f"\nWe do not have {theMovie} in our store.")
        else:
            print(f"\n{theClient} is not in the client list.")

    # RETURN SECTION
    def returnMovies(self, theClient, theMovie):
        if theClient in self.clientNameList():
            if theMovie in self.movieNameList():
                if theMovie in self.clientsRepository.getClient(theClient).rentedMovies:
                    self.clientsRepository.removeMovie(self.moviesRepository.getMovie(theMovie).title)
                    self.moviesRepository.getMovie(theMovie).availability = "Available"
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
                print(client + " | Rented: " + str(len(self.clientsRepository.getClient(client).rentedMovies)) + " movie/s")

    # DISPLAY THE MOST RENTED MOVIE
    def displayMostRentedMovies(self):
        values = [count for movie, count in self.moviesRepository.trackRentedMovies.items()]
        if max(values) != 0:
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
