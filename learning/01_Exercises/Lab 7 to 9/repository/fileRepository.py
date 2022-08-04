from domain.entity import client, movie
from abc import ABC, abstractmethod


class fileRepository(ABC):
    @abstractmethod
    def update(self, ID, item):
        pass

    @abstractmethod
    def save(self, item):
        pass

    def saveAll(self, items):
        for item in items:
            self.save(item)

    @abstractmethod
    def getAll(self):
        pass

    def remove(self, ID):
        updateRepo = [item for item in self.getAll() if ID != item.id]
        return updateRepo

    def getID(self):
        if len(self.getAll()) == 0:
            return []
        else:
            file = open(self.fileName, "r")
            lines = file.readlines()
            ID = 0
            idList = [line.split(":")[ID].strip() for line in lines]
            file.close()
            return idList

    def removeAll(self):
        file = open(self.fileName, "w")
        file.close()

    def getNames(self):
        file = open(self.fileName, "r")
        lines = file.readlines()
        listWithNames = []
        name = 1

        for info in lines:
            info = info.split(":")
            listWithNames.append(info[name].strip())
        file.close()
        return listWithNames


class clientFileRepository(fileRepository):
    def __init__(self):
        self.fileName = "repository/clients.text"
        self.trackClientRentedMovies = {}
        self.currentCount = 0
        self.currentID = 1

    def getAll(self):
        with open(self.fileName, "r") as file:
            lines = file.readlines()
            clientsList = []
            uniqueNr, name, CNP, rentedMovies = 0, 1, 2, 3

            for info in lines:
                info = info.split(":")
                clientInfo = client(info[name].strip(), info[CNP].strip())
                clientInfo.id = info[uniqueNr].strip()
                # Review below line of code.
                if len(clientInfo.rentedMovies) == 0:
                    pass
                clientsList.append(clientInfo)
            return clientsList

    def save(self, clientInfo):
        with open(self.fileName, "a") as file:
            if len(self.getAll()) == 0:
                clientInfo.id = self.currentID
            else:
                clientInfo.id = int(self.getAll()[-1].id) + 1
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

    # Review the code below
    def saveMovie(self, theClient, theMovie):
        for clientInfo in self.getAll():
            if theClient == clientInfo.name:
                clientInfo.rentedMovies.append(theMovie)

    def addCount(self, theClient):
        self.trackClientRentedMovies[theClient] += 1


class moviesFileRepository(fileRepository):
    def __init__(self):
        self.fileName = "repository/movies.text"
        self.currentAvailability = "Available"
        self.trackRentedMovies = {}
        self.currentID = 1

    def getAll(self):
        with open(self.fileName, "r") as file:
            lines = file.readlines()
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
            movieInfo.availability = self.currentAvailability
            file.write(str(movieInfo) + "\n")

    def update(self, ID, newMovie):
        updatedList = []
        for movieInfo in self.getAll():
            if ID == movieInfo.id:
                movieInfo.title = newMovie.title
                movieInfo.description = newMovie.description
                movieInfo.genre = newMovie.genre
                updatedList.append(movieInfo)
            else:
                updatedList.append(movieInfo)
        self.removeAll(), self.saveAll(updatedList)

    def getMovie(self, theMovie):
        for movieInfo in self.getAll():
            if theMovie == movieInfo.title:
                return movieInfo

    def getMovieAvailability(self, theMovie):
        with open(self.fileName, "r") as file:
            lines = file.readlines()
            title = 1
            availability = 4

            for info in lines:
                info = info.split(":")
                if info[title].strip() == theMovie:
                    return info[availability].strip()

    def addCount(self, theMovie):
        self.trackRentedMovies[theMovie] += 1
