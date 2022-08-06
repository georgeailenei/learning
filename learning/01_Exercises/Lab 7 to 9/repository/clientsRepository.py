from repository.repository import repository


class clientsRepository(repository):
    def __init__(self):
        self.database = []
        self.currentID = 1
        self.trackClientRentedMovies = {}
        self.rentedMovies = ""
        self.currentCount = 0

    def save(self, client):
        client.id = self.currentID
        self.database.append(client)
        self.trackClientRentedMovies[client.name] = self.currentCount
        self.currentID += 1

    def addCount(self, client):
        self.trackClientRentedMovies[client] += 1

    def update(self, ID, newClient):
        updatedDatabase = []
        for client in self.database:
            if ID in str(client.id):
                client.name = newClient.name
                client.CNP = newClient.CNP
                updatedDatabase.append(client)
            else:
                updatedDatabase.append(client)
        self.removeAll(), self.saveAll(updatedDatabase)

    def getNames(self):
        nameList = [client.name for client in self.database]
        return nameList

    def getClient(self, theClient):
        for client in self.getAll():
            if theClient == client.name:
                return client

    def saveMovie(self, theClient, movie):
        for client in self.database:
            if theClient == client.name:
                client.rentedMovies = client.rentedMovies + " " + movie + ";"

    def removeMovie(self, movie):
        for client in self.database:
            if movie in client.rentedMovies:
                movieList = str(client.rentedMovies).split(";")
                movieList = [name.strip() for name in movieList]
                movieList.remove(movie)
                client.rentedMovies = "; ".join(movieList)

    def getMovieCount(self, theClient):
        for client in self.getAll():
            if client.name == theClient:
                movieList = str(client.rentedMovies).split(";")
                count = len(movieList) - 1
                return count

    def get(self):
        pass
