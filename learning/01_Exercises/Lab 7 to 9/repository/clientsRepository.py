from repository.repository import repository


class clientsRepository(repository):
    def __init__(self):
        self.clients = []
        self.currentID = 1

    def save(self, client):
        # Save the client given by the user and implement a unique ID.
        client.id = self.currentID
        self.clients.append(client)
        self.currentID += 1

    def remove(self):
        pass

    def getAll(self):
        # Get the list with the clients.
        return self.clients
