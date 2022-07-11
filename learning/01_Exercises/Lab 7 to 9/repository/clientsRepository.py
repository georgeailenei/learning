from repository.repository import repository


class clientsRepository(repository):
    def __init__(self):
        self.clients = []
        self.currentID = 1

    def save(self, client):
        self.clients.append(client)
        return self.clients

    def remove(self):
        pass

    def getAll(self):
        return self.clients
