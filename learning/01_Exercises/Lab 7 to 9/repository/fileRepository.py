from domain.entity import client, movie
from abc import ABC, abstractmethod


class fileRepository(ABC):
    @abstractmethod
    def update(self, ID, item):
        pass

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def getNames(self):
        pass

    @abstractmethod
    def save(self, item):
        pass

    def saveAll(self, items):
        for item in items:
            self.save(item)

    def remove(self, ID):
        updateRepo = [item for item in self.getAll() if ID != item.id]
        return updateRepo

    def removeAll(self):
        file = open(self.fileName, "w")
        file.close()

    def getIdList(self):
        if len(self.getAll()) == 0:
            return []
        else:
            idList = [item.id for item in self.getAll()]
            return idList


class clientFileRepository(fileRepository):
    def __init__(self):
        self.fileName = "repository/clients.text"
        self.trackClientRentedMovies = {}
        self.rentedMovies = ""
        self.currentCount = 0
        self.currentID = 1

    def addCount(self, theClient):
        self.trackClientRentedMovies[theClient] += 1

    def getAll(self):
        file = open(self.fileName, "r")

        lines = file.readlines()
        if len(lines) == 0:
            return []
        else:
            clientsList = []
            uniqueNr, name, CNP, rentedMovies = 0, 1, 2, 3

            for info in lines:
                info = info.split(":")
                clientInfo = client(info[name].strip(), info[CNP].strip())
                clientInfo.id = info[uniqueNr].strip()
                clientInfo.rentedMovies = info[rentedMovies].strip()
                clientsList.append(clientInfo)
            return clientsList

    def save(self, clientInfo):
        with open(self.fileName, "a") as file:
            if len(self.getAll()) == 0:
                clientInfo.id = self.currentID
            else:
                clientInfo.id = int(self.getAll()[-1].id) + 1

            if len(self.rentedMovies) < len(clientInfo.rentedMovies):
                pass
            else:
                clientInfo.rentedMovies = self.rentedMovies

            self.trackClientRentedMovies[clientInfo.name] = self.currentCount
            file.write(str(clientInfo) + "\n")

    def update(self, ID, newClient):
        updatedList = []
        for clientInfo in self.getAll():
            if ID == clientInfo.id:
                clientInfo.name = newClient.name
                clientInfo.CNP = newClient.CNP
                clientInfo.rentedMovies = newClient.rentedMovies
                updatedList.append(clientInfo)
            else:
                updatedList.append(clientInfo)
        self.removeAll(), self.saveAll(updatedList)

    def saveMovie(self, theClient, theMovie):
        for clientInfo in self.getAll():
            if theClient == clientInfo.name:
                clientInfo.rentedMovies = clientInfo.rentedMovies + " " + theMovie + ";"
                self.update(clientInfo.id, clientInfo)

    def removeMovie(self, theMovie):
        for clientInfo in self.getAll():
            if theMovie in clientInfo.rentedMovies:
                movieList = str(clientInfo.rentedMovies).split(";")
                movieList = [name.strip() for name in movieList]
                movieList.remove(theMovie)
                clientInfo.rentedMovies = "; ".join(movieList)
                self.update(clientInfo.id, clientInfo)

    def getNames(self):
        clientNames = [clientInfo.name for clientInfo in self.getAll()]
        return clientNames

    def getClient(self, theClient):
        for clientInfo in self.getAll():
            if theClient == clientInfo.name:
                return clientInfo

    def getID(self, theClient):
        for clientInfo in self.getAll():
            if clientInfo.name == theClient:
                return clientInfo.id

    def getMovieCount(self, theClient):
        for clientInfo in self.getAll():
            if clientInfo.name == theClient:
                movieList = str(clientInfo.rentedMovies).split(";")
                count = len(movieList) - 1
                return count


class moviesFileRepository(fileRepository):
    def __init__(self):
        self.fileName = "repository/movies.text"
        self.currentAvailability = "Available"
        self.trackRentedMovies = {}
        self.currentID = 1

    def addCount(self, theMovie):
        self.trackRentedMovies[theMovie] += 1

    def getAll(self):
        file = open(self.fileName, "r")

        lines = file.readlines()
        if len(lines) == 0:
            return []
        else:
            movieList = []
            uniqueNr, title, description, genre, availability = 0, 1, 2, 3, 4

            for info in lines:
                info = info.split(":")
                movieInfo = movie(info[title].strip(), info[description].strip(), info[genre].strip())
                movieInfo.id = info[uniqueNr].strip()
                movieInfo.availability = info[availability].strip()
                movieList.append(movieInfo)
            return movieList

    def save(self, movieInfo):
        with open(self.fileName, "a") as file:
            if len(self.getAll()) == 0:
                movieInfo.id = self.currentID
            else:
                movieInfo.id = int(self.getAll()[-1].id) + 1

            if len(self.currentAvailability) < len(str(movieInfo.availability)):
                pass
            else:
                movieInfo.availability = self.currentAvailability

            if movieInfo.title not in self.trackRentedMovies:
                self.trackRentedMovies[movieInfo.title] = 0

            file.write(str(movieInfo) + "\n")

    def update(self, ID, newMovie):
        updatedList = []
        for movieInfo in self.getAll():
            if ID == movieInfo.id:
                movieInfo.title = newMovie.title
                movieInfo.description = newMovie.description
                movieInfo.genre = newMovie.genre
                movieInfo.availability = newMovie.availability
                updatedList.append(movieInfo)
            else:
                updatedList.append(movieInfo)
        self.removeAll(), self.saveAll(updatedList)

    def getMovie(self, theMovie):
        for movieInfo in self.getAll():
            if theMovie == movieInfo.title:
                return movieInfo

    def getNames(self):
        movieNames = [movieInfo.title for movieInfo in self.getAll()]
        return movieNames

    def getID(self, theMovie):
        for movieInfo in self.getAll():
            if movieInfo.title == theMovie:
                return movieInfo.id

    def updateStatus(self, theMovie):
        if theMovie.availability == "Available":
            theMovie.availability = "NOT AVAILABLE"
            self.update(self.getID(theMovie.title), theMovie)
        elif theMovie.availability == "NOT AVAILABLE":
            theMovie.availability = "Available"
            self.update(self.getID(theMovie.title), theMovie)
