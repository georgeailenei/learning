
class ControllerError(Exception):
    pass


class Controller:
    def __init__(self, moviesRepository, clientsRepository, validatorForMovie, validatorForClient):
        self.moviesRepository = moviesRepository
        self.clientsRepository = clientsRepository
        self.validatorForMovie = validatorForMovie
        self.validatorForClient = validatorForClient

    def addClient(self, Client):
        self.clientsRepository.save(Client)

    def addMovie(self, movie):
        "Aici imi crapa codul... Inca nu-mi dau seama ce scriu gresit"
        # if self.validatorForMovie.checkGenre(movie.genre):
        self.moviesRepository.save(movie)
        # else:
        #     print("Ceva")

    def movieList(self):
        return self.moviesRepository.getAll()

    def clientList(self):
        return self.clientsRepository.getAll()
