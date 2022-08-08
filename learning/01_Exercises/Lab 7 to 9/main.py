from UI.userInterface import UI
from services.controller import Controller
from repository.moviesRepository import MoviesRepository
from repository.clientsRepository import ClientsRepository
from repository.fileRepository import ClientFileRepository
from repository.fileRepository import MoviesFileRepository
from domain.validator import MovieValidator
from domain.validator import ClientValidator
from domain.entity import Movie, Client


def main():
    validatorForMovie = MovieValidator()
    validatorForClient = ClientValidator()
    moviesRepo = MoviesFileRepository()
    clientsRepo = ClientFileRepository()
    controller = Controller(moviesRepo, clientsRepo, validatorForMovie, validatorForClient)

    # Some movie samples
    controller.addMovie(Movie("Avengers", "The Avengers were a team of extraordinary individuals.", "Action"))
    controller.addMovie(Movie("Never Back Down", "It tells the story of a frustrated and conflicted teenager.", "Romance"))
    controller.addMovie(Movie("Batman", "Is the superhero protector of Gotham City.", "Crime"))

    # Some client samples
    controller.addClient(Client("George", "459"))
    controller.addClient(Client("Shawn", "879"))
    controller.addClient(Client("Dan", "687"))

    userInterface = UI(controller)
    userInterface.run()


if __name__ == "__main__":
    main()
