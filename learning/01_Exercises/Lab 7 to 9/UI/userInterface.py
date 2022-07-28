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

    removeSubMenu = "1. Remove movies\n" \
                    "2. Remove clients\n" \
                    "3. Return to Main Menu"

    updateSubMenu = "1. Update movies\n" \
                    "2. Update clients\n" \
                    "3. Return to Main Menu"

    searchSubMenu = "1. Search for movies\n" \
                    "2. Search for clients\n" \
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

    def rmvSubMenu(self):
        # It displays the sub menu for the Remove section.
        print(self.removeSubMenu)

    def updSubMenu(self):
        # It displays the sub menu for the Remove section.
        print(self.updateSubMenu)

    def findingSubMenu(self):
        # It displays the sub menu for Search section.
        print(self.searchSubMenu)

    def exit(self):
        # The method takes and input from the user, and it returns True or False.
        option = input("Do you want to continue (N/Y): ")
        if option == "N":
            return False
        elif option == "Y":
            return True

    def refreshScreen(self):
        return os.system("cls")

    def collectWord(self):
        # Ask the user for a word.
        word = input("Search: ")
        return word

    def collectID(self):
        # Ask the user for an ID.
        print("\nPlease insert an ID")
        ID = input("Write ID: ")
        return ID

    def collectMovieData(self):
        # Collects the data from the user, and it returns an entity/object.
        print("\nPlease insert the following information")
        title = input("Movie title: ")
        description = input("Description: ")
        genre = input("Genre: ")
        return movie(title, description, genre)

    def collectClientsData(self):
        # Collects the data from the user, and it returns an entity/object.
        print("\nPlease insert the following information")
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
            print("ADD MOVIES")
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
            print("ADD CLIENTS")
            self.displayClients()

            # Collect a new client from the user.
            Client = self.collectClientsData()

            # Try/add the client to the client list/clientRepo.
            self.controller.addClient(Client)

            # Ask the user if he wants to continue or not.
            if not self.exit():
                break

    def removeMovies(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title and the current list with clients.
            print("REMOVE MOVIES")
            self.displayMovies()

            # Collect the movie ID.
            ID = self.collectID()

            # Try/remove the movie with the ID given.
            self.controller.removeMovie(ID)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def removeClient(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title and the current list with clients.
            print("REMOVE CLIENTS")
            self.displayClients()

            # Collect the movie ID.
            ID = self.collectID()

            # Try/remove the movie with the ID given.
            self.controller.removeClient(ID)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def updateMovies(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title and the current list with clients.
            print("UPDATE MOVIES")
            self.displayMovies()

            # Collect the movie ID.
            ID = self.collectID()
            if not self.controller.validatorForMovie.checkID(ID, self.controller.movieIDList()):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Collect new data to update the list.
            newMovie = self.collectMovieData()
            if not self.controller.validatorForMovie.validator(newMovie):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Try to update by ID.
            self.controller.updateMovie(ID, newMovie)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def updateClients(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title and the current list with clients.
            print("UPDATE CLIENTS")
            self.displayClients()

            # Collect the client's ID.
            ID = self.collectID()
            if not self.controller.validatorForClient.checkID(ID, self.controller.clientIDList()):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Collect new data to update the list.
            newClient = self.collectClientsData()
            if not self.controller.validatorForClient.validator(newClient):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Try to update by ID.
            self.controller.updateClient(ID, newClient)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def searchMovies(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title.
            print("SEARCH FOR MOVIES")

            # Collect the name of the movie.
            findMovie = self.collectWord()

            # Try to find the movie in the movie database.
            self.controller.searchMovies(findMovie)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def searchClients(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title.
            print("SEARCH FOR CLIENTS")

            # Collect the name of the movie.
            findClient = self.collectWord()

            # Try to find the movie in the movie database.
            self.controller.searchClients(findClient)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def start(self):
        while True:
            self.refreshScreen(), self.mainMenu()
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
                while True:
                    self.refreshScreen(), self.rmvSubMenu()
                    option = self.userInput()

                    if option == "1":
                        self.removeMovies()
                    elif option == "2":
                        self.removeClient()
                    elif option == "3":
                        break

            elif option == "3":
                while True:
                    self.refreshScreen(), self.updSubMenu()
                    option = self.userInput()

                    if option == "1":
                        self.updateMovies()
                    elif option == "2":
                        self.updateClients()
                    elif option == "3":
                        break

            elif option == "4":
                while True:
                    self.refreshScreen(), self.findingSubMenu()
                    option = self.userInput()

                    if option == "1":
                        self.searchMovies()
                    elif option == "2":
                        self.searchClients()
                    elif option == "3":
                        break

            elif option == "8":
                break
