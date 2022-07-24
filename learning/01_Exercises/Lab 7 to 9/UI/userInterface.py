from abc import ABC, abstractmethod
from domain.entity import movie, client
import os


class UI(ABC):
    @abstractmethod
    def userInput(self):
        pass


class consoleUI(UI):
    mainTitle = "This app manages movies and clients for Company X"
    Menu = '1. Add\n' \
           '2. Remove\n' \
           '3. Update\n' \
           '4. Search\n' \
           '5. Rent\n' \
           '6. Returns\n' \
           '7. Reports\n' \
           '8. Exit'

    addSubMenu = "1. Add movies\n" \
                 "2. Add clients\n" \
                 "3. Return to Main Menu"

    def __init__(self, controller):
        self.controller = controller

    def userInput(self):
        # Takes and input from the user.
        option = input("Choose option: ")
        return option

    def mainMenu(self):
        # It displays the title and the main menu.
        print(self.mainTitle)
        print(self.Menu)

    def subMenu(self):
        # It displays the sub menu for the Add section.
        print(self.addSubMenu)

    def exit(self):
        # The method takes and input from the user, and it returns True or False.
        option = input("Do you want to continue (N/Y): ")
        if option == "N":
            return False
        elif option == "Y":
            return True

    def refreshScreen(self):
        return os.system("cls")

    def collectMovieData(self):
        # Collects the data from the user, and it returns an entity/object.
        print("Please insert the following information")
        title = input("Movie title: ")
        description = input("Description: ")
        genre = input("Genre: ")
        return movie(title, description, genre)

    def collectClientsData(self):
        # Collects the data from the user, and it returns an entity/object.
        print("Please insert the following information")
        name = input("Name: ")
        CNP = input("CNP: ")
        return client(name, CNP)

    def displayMovies(self):
        # It prints all the movies that are currently in movieRepo.
        print("This is the current list with movies")
        allMovies = self.controller.movieList()
        if len(allMovies) == 0:
            print("- no movies")
        for m in allMovies:
            print(m)

    def displayClients(self):
        # It prints all the movies that are currently in clientRepo.
        print("This is the current list with clients")
        allClients = self.controller.clientList()
        if len(allClients) == 0:
            print("- no clients")
        for Client in allClients:
            print(Client)

    def addMovie(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title and the current list with movies.
            print("Here you can add movies")
            self.displayMovies()

            # Collect a new movie from the user.
            newMovie = self.collectMovieData()

            # Try/add the movie to the movie list/movieRepo.
            self.controller.addMovie(newMovie)

            # Ask the user if he wants to continue or not.
            if not self.exit():
                break

    def addClients(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title and the current list with clients.
            print("Here you can add clients")
            self.displayClients()

            # Collect a new client from the user.
            Client = self.collectClientsData()

            # Try/add the client to the client list/clientRepo.
            self.controller.addClient(Client)

            # Ask the user if he wants to continue or not.
            if not self.exit():
                break

    def start(self):
        while True:
            self.refreshScreen()
            self.mainMenu()
            option = self.userInput()

            if option == "1":
                while True:
                    self.refreshScreen()
                    self.subMenu()
                    option = self.userInput()

                    if option == "1":
                        self.addMovie()

                    elif option == "2":
                        self.addClients()

                    elif option == "3":
                        break

            elif option == "2":
                pass

            elif option == "8":
                break
