from abc import ABC, abstractmethod
from domain.entity import movies, client


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

    def __init__(self, controller):
        self.controller = controller

    def userInput(self):
        option = input("Choose option: ")
        return option

    def mainMenu(self):
        print(self.mainTitle)
        print(self.Menu)

    def collectMovieData(self):
        title = input("Title: ")
        description = input("Description: ")
        gender = input("Gender: ")
        return movies(title, description, gender)

    def collectClientsData(self):
        name = input("Name: ")
        CNP = input("CNP: ")
        return client(name, CNP)

    def displayMovies(self):
        print("This is the current list with movies")
        allMovies = self.controller.movieList()
        for movie in allMovies:
            print(movie)

    def addMovie(self):
        while True:
            print("Here you can add movies\n")
            self.displayMovies()
            movie = self.collectMovieData()
            self.controller.addMovie(movie)

    def start(self):
        while True:
            self.mainMenu()
            option = self.userInput()

            if option == "1":
                self.addMovie()

