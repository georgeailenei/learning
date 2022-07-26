from UI.userInterface import consoleUI
from services.controller import Controller
from repository.moviesRepository import moviesRepository
from repository.clientsRepository import clientsRepository
from domain.validator import movieValidator
from domain.validator import clientValidator
from domain.entity import movie


def main():
    validatorForMovie = movieValidator()
    validatorForClient = clientValidator()
    moviesRepo = moviesRepository()
    clientsRepo = clientsRepository()
    controller = Controller(moviesRepo, clientsRepo, validatorForMovie, validatorForClient)
    controller.addMovie(movie("Avengers", "CevaDes", "Action"))
    userInterface = consoleUI(controller)
    userInterface.start()


if __name__ == "__main__":
    main()
