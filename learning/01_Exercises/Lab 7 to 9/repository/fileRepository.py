from domain.entity import client, movie
from abc import ABC, abstractmethod


class fileRepository(ABC):
    def save(self, item):
        file = open(self.fileName, "a")
        size = len(self.getAll())
        ID = 0

        if size == 0:
            item.id = self.currentID
        else:
            lastLine = self.getAll()[-1].split()
            item.id = int(lastLine[ID]) + 1

        file.write(str(item) + "\n")
        file.close()

    @abstractmethod
    def remove(self, ID):
        pass

    def saveAll(self, items):
        for item in items:
            self.save(item)

    def getAll(self):
        file = open(self.fileName, "r")
        lines = file.readlines()
        file.close()
        return lines

    def getID(self):
        if len(self.getAll()) == 0:
            return []
        else:
            file = open(self.fileName, "r")
            lines = file.readlines()
            ID = 0
            idList = [line.split()[ID] for line in lines]
            file.close()
            return idList

    def removeAll(self):
        file = open(self.fileName, "w")
        file.close()


class clientFileRepository(fileRepository):
    def __init__(self):
        self.fileName = "repository/clients.text"
        self.currentID = 1

    def remove(self, ID):
        file = open(self.fileName, "r")
        lines = file.readlines()
        uniqueNr, name, CNP = 0, 2, 4

        updatedList = []
        for info in lines:
            if ID != info.split()[uniqueNr]:
                updatedList.append(client(info.split()[name], info.split()[CNP]))
        file.close()
        return updatedList


class moviesFileRepository(fileRepository):
    def __init__(self):
        self.fileName = "repository/movies.text"
        self.currentID = 1

    def remove(self, ID):
        file = open(self.fileName, "r")
        lines = file.readlines()
        uniqueNr, title, description, genre = 0, [], [], []

        updatedList = []
        count = 4

        for info in lines:
            if ID != info.split()[uniqueNr]:
                for word in range(count, len(info)):
                    if info[word] != "|":
                        title.append(info[word])
                    else:
                        count = info.index(info[word]) + 1
                        break

                title = "".join(title[:-1])

                for word in range(count, len(info)):
                    if info[word] != "|":
                        description.append(info[word])
                    else:
                        count = info.index(info[word]) + 1
                        break

                description = "".join(description[1:-1])
                updatedList.append(movie(title, description, genre))

        file.close()
        return updatedList
