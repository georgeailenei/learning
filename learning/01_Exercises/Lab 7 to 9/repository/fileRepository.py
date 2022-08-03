
class fileRepository:
    def save(self, item):
        file = open(self.fileName, "a")
        size = len(self.getAll())
        ID = 0

        if size == 0:
            item.id = self.currentID
        else:
            lastLine = self.getAll()[-1].split()
            item.id = int(lastLine[ID]) + 1

        file.write(item.__repr__() + "\n")
        file.close()

    def getAll(self):
        file = open(self.fileName, "r")
        lines = file.readlines()
        file.close()
        return lines


class clientFileRepository(fileRepository):
    def __init__(self):
        self.fileName = "repository/clients.text"
        self.currentID = 1


class moviesFileRepository(fileRepository):
    def __init__(self):
        self.fileName = "repository/movies.text"
        self.currentID = 1
