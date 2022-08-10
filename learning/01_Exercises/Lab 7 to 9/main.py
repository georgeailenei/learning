from UI.userInterface import Ui
from services.controller import Controller
from repository.moviesRepository import MoviesRepository
from repository.clientsRepository import ClientsRepository
from repository.fileRepository import ClientFileRepository
from repository.fileRepository import MoviesFileRepository
from domain.validator import ValidateMovie
from domain.validator import ValidateClient
from domain.entity import Movie, Client


def main():
    validatorForMovie = ValidateMovie()
    validatorForClient = ValidateClient()
    moviesRepo = MoviesFileRepository("repository/movies.text")
    clientsRepo = ClientFileRepository()
    controller = Controller(moviesRepo, clientsRepo, validatorForMovie, validatorForClient)

    # Some movie samples
    controller.add_movie(Movie("Avengers", "The Avengers were a team of extraordinary individuals.", "Action"))
    controller.add_movie(Movie("Never Back Down", "It tells the story of a frustrated and conflicted teenager.", "Romance"))
    controller.add_movie(Movie("Batman", "Is the superhero protector of Gotham City.", "Crime"))

    # Some client samples
    controller.add_client(Client("George", "459"))
    controller.add_client(Client("Shawn", "879"))
    controller.add_client(Client("Dan", "687"))

    userInterface = Ui(controller)
    userInterface.run()


if __name__ == "__main__":
    main()
