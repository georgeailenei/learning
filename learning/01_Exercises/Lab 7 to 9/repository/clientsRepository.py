from repository.repository import repository


class clientsRepository(repository):
    def __init__(self):
        self.database = []
        self.currentID = 1

    def update(self, ID, newClient):
        updatedDatabase = []
        for client in self.database:
            if ID in client.__repr__():
                client.name = newClient.name
                client.CNP = newClient.CNP
                updatedDatabase.append(client)
            else:
                updatedDatabase.append(client)
        self.removeAll(), self.saveAll(updatedDatabase)

    def getNames(self):
        nameList = [client.name for client in self.database]
        return nameList
