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
        option = input("Choose option: ")
        return option

    def mainMenu(self):
        print(self.mainTitle)
        print(self.Menu)

    def subMenu(self):
        print(self.addSubMenu)

    def exit(self):
        option = input("Do you want to continue (N/Y): ")
        if option == "N":
            return False
        elif option == "Y":
            return True

    def refreshScreen(self):
        return os.system("cls")

    def collectMovieData(self):
        print("Please insert the following information")
        title = input("Title: ")
        description = input("Description: ")
        genre = input("Genre: ")
        return movie(title, description, genre)

    def collectClientsData(self):
        print("Please insert the following information")
        name = input("Name: ")
        CNP = input("CNP: ")
        return client(name, CNP)

    def displayMovies(self):
        print("This is the current list with movies")
        allMovies = self.controller.movieList()
        for movie in allMovies:
            print(movie)

    def displayClients(self):
        print("This is the current list with clients")
        allClients = self.controller.clientList()
        for Client in allClients:
            print(Client)

    def addMovie(self):
        while True:
            self.refreshScreen()
            print("Here you can add movies")
            self.displayMovies()
            movie = self.collectMovieData()
            self.controller.addMovie(movie)
            if not self.exit():
                break

    def addClients(self):
        while True:
            self.refreshScreen()
            print("Here you can add clients")
            self.displayClients()
            Client = self.collectClientsData()
            self.controller.addClient(Client)
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

            elif option == "8":
                break
