
class Controller:
    def __init__(self, moviesRepository, clientsRepository):
        self.moviesRepository = moviesRepository
        self.clientsRepository = clientsRepository

    def addClient(self):
        pass

    def addMovie(self, movie):
        self.moviesRepository.save(movie)

    def movieList(self):
        return self.moviesRepository.getAll()

    def clientList(self):
        return self.clientsRepository.getAll()
