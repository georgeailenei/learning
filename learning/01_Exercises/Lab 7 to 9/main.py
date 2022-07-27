from UI.userInterface import consoleUI
from services.controller import Controller
from repository.moviesRepository import moviesRepository
from repository.clientsRepository import clientsRepository
from domain.validator import movieValidator
from domain.validator import clientValidator
from domain.entity import movie, client


def main():
    validatorForMovie = movieValidator()
    validatorForClient = clientValidator()
    moviesRepo = moviesRepository()
    clientsRepo = clientsRepository()
    controller = Controller(moviesRepo, clientsRepo, validatorForMovie, validatorForClient)

    # Same movie samples
    controller.addMovie(movie("Avengers", "The Avengers were a team of extraordinary individuals.", "Action"))
    controller.addMovie(movie("Never Back Down", "It tells the story of a frustrated and conflicted teenager.", "Romance"))
    controller.addMovie(movie("Batman", "Is the superhero protector of Gotham City.", "Crime"))

    # Same client samples
    controller.addClient(client("George", "459"))
    controller.addClient(client("Shawn", "879"))
    controller.addClient(client("Dan", "687"))

    userInterface = consoleUI(controller)
    userInterface.start()


if __name__ == "__main__":
    main()
