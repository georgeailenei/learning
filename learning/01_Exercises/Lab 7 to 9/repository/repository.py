from abc import ABC, abstractmethod


class repository(ABC):
    @abstractmethod
    def save(self, item):
        pass

    def saveAll(self, items):
        # Save all the movies to the movieRepo.
        self.currentID = 1
        for movie in items:
            self.save(movie)
        return self.database

    def remove(self, ID):
        # Remove the desired movie by saving all the other movies in a new list.
        updateRepo = [item for item in self.database if ID not in item.__repr__()]
        return updateRepo

    def removeAll(self):
        # Remove all the items from the list.
        return self.database.clear()

    def getAll(self):
        # Get the list with the movies.
        return self.database

    def getID(self):
        idList = [item.id.__repr__() for item in self.database]
        return idList

    @abstractmethod
    def update(self):
        pass
