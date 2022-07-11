from UI.userInterface import consoleUI
from services.controller import Controller
from repository.moviesRepository import moviesRepository
from repository.clientsRepository import clientsRepository


def main():
    moviesRepo = moviesRepository()
    clientsRepo = clientsRepository()
    controller = Controller(moviesRepo, clientsRepo)
    userInterface = consoleUI(controller)
    userInterface.start()


if __name__ == "__main__":
    main()
