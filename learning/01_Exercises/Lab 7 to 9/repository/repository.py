from abc import ABC, abstractmethod


class repository(ABC):
    @abstractmethod
    def save(self, item):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get(self):
        pass

    def saveAll(self, items):
        self.currentID = 1
        for movie in items:
            self.save(movie)
        return self.database

    def remove(self, ID):
        updateRepo = [item for item in self.database if ID not in item.__repr__()]
        return updateRepo

    def removeAll(self):
        return self.database.clear()

    def getAll(self):
        return self.database

    def getID(self):
        idList = [item.id.__repr__() for item in self.database]
        return idList
