from domain.entity import Movie, Client
import os


class UI:
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

    reportsSubMenu = "1. Display clients\n" \
                     "2. Display most rented movies\n" \
                     "3. Display top 3 clients with most rented movies\n" \
                     "4. Return to Main Menu"

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

    def rmvSubMenu(self):
        print(self.removeSubMenu)

    def updSubMenu(self):
        print(self.updateSubMenu)

    def findingSubMenu(self):
        print(self.searchSubMenu)

    def reportSubMenu(self):
        print(self.reportsSubMenu)

    def exit(self):
        option = input("Do you want to continue (N/Y): ")
        if option == "N":
            return False
        elif option == "Y":
            return True

    def refreshScreen(self):
        return os.system("cls")

    def collectWord(self):
        word = input("Search: ")
        return word

    def collectID(self):
        print("\nPlease insert an ID")
        ID = input("Write ID: ")
        return ID

    def collectMovieData(self):
        print("\nPlease insert the following information")
        title = input("Movie title: ")
        description = input("Description: ")
        genre = input("Genre: ")
        return Movie(title, description, genre)

    def collectClientsData(self):
        print("\nPlease insert the following information")
        name = input("Name: ")
        CNP = input("CNP: ")
        return Client(name, CNP)

    def displayMovies(self):
        print("This is the current list with movies")
        allMovies = self.controller.moviesRepository.getAll()
        if len(allMovies) == 0:
            print("- no movies")
        else:
            for theMovie in allMovies:
                print(theMovie)

    def displayClients(self):
        print("This is the current list with clients")
        allClients = self.controller.clientsRepository.getAll()
        if len(allClients) == 0:
            print("- no clients info")
        for clientInfo in allClients:
            print(clientInfo)

    def displayMoviesCount(self):
        print("The current count for each movie")
        for theMovie, theCount in self.controller.moviesRepository.trackRentedMovies.items():
            print(theMovie, theCount)

    def displayClientsMovieCount(self):
        print("The current list with clients and their rented movie count")
        for theClient, theCount in self.controller.clientsRepository.trackClientRentedMovies.items():
            print(theClient, theCount)

    def displayTop30Clients(self, clients):
        for client, count in clients.items():
            print(client, count)

    def addMovie(self):
        while True:
            self.refreshScreen()
            print("ADD MOVIES")

            self.displayMovies()
            newMovie = self.collectMovieData()
            self.controller.addMovie(newMovie)
            if not self.exit():
                break

    def addClients(self):
        while True:
            self.refreshScreen()
            print("ADD CLIENTS")

            self.displayClients()
            Client = self.collectClientsData()
            self.controller.addClient(Client)
            if not self.exit():
                break

    def removeMovies(self):
        while True:
            self.refreshScreen()
            print("REMOVE MOVIES")

            self.displayMovies()
            ID = self.collectID()
            self.controller.removeMovie(ID)
            if not self.exit():
                break

    def removeClient(self):
        while True:
            self.refreshScreen()
            print("REMOVE CLIENTS")
            self.displayClients()

            ID = self.collectID()
            self.controller.removeClient(ID)
            if not self.exit():
                break

    def updateMovies(self):
        while True:
            self.refreshScreen()
            print("UPDATE MOVIES")
            self.displayMovies()

            # Collect the movie ID.
            ID = self.collectID()
            if not self.controller.validatorForMovie.checkID(ID, self.controller.moviesRepository.getIdList()):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Collect new data to update the list.
            newMovie = self.collectMovieData()
            if not self.controller.validatorForMovie.validator(newMovie, self.controller.moviesRepository.getNames()):
                # You must raise an error/message for the user to know what's going on.
                continue

            self.controller.updateMovie(ID, newMovie)
            if not self.exit():
                break

    def updateClients(self):
        while True:
            self.refreshScreen()
            print("UPDATE CLIENTS")
            self.displayClients()

            # Collect the client's ID.
            ID = self.collectID()
            if not self.controller.validatorForClient.checkID(ID, self.controller.clientsRepository.getIdList()):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Collect new data to update the list.
            newClient = self.collectClientsData()
            if not self.controller.validatorForClient.validator(newClient, self.controller.clientsRepository.getNames()):
                # You must raise an error/message for the user to know what's going on.
                continue

            self.controller.updateClient(ID, newClient)
            if not self.exit():
                break

    def searchMovies(self):
        while True:
            self.refreshScreen()
            print("SEARCH FOR MOVIES")

            findMovie = self.collectWord()
            self.controller.searchMovies(findMovie)
            if not self.exit():
                break

    def searchClients(self):
        while True:
            self.refreshScreen()
            print("SEARCH FOR CLIENTS")

            findClient = self.collectWord()
            self.controller.searchClients(findClient)
            if not self.exit():
                break

    def rentMovies(self):
        while True:
            self.refreshScreen()

            print("RENT MOVIES")
            self.displayMovies()

            print("\nTHE CLIENT LIST")
            self.displayClients()

            theClient = input("Choose a client: ")
            theMovie = input("Choose a movie: ")
            self.controller.rentMovies(theClient, theMovie)
            if not self.exit():
                break

    def returnMovies(self):
        while True:
            self.refreshScreen()
            print("RETURN MOVIES")
            self.displayMovies()

            print("\nTHE CLIENT LIST")
            self.displayClients()

            theClient = input("Choose a client: ")
            theMovie = input("Choose a movie: ")

            self.controller.returnMovies(theClient, theMovie)
            if not self.exit():
                break

    def displayClientsInOrder(self):
        while True:
            self.refreshScreen()
            print("DISPLAY CLIENTS WITH MOVIES")

            self.controller.displayClientsInOrder()
            if not self.exit():
                break

    def displayMostRentedMovies(self):
        while True:
            self.refreshScreen()
            self.displayMoviesCount()

            print("\nMost rented movie: ")
            self.controller.displayMostRentedMovies()
            if not self.exit():
                break

    def displayClientsWithMostMovies(self):
        while True:
            self.refreshScreen()
            self.displayClientsMovieCount()

            print("\nTOP 30% clients are: ")
            top30 = self.controller.displayClientsWithMostMovies()
            self.displayTop30Clients(top30)
            if not self.exit():
                break

    def run(self):
        # Load Statistics
        self.controller.clientsRepository.loadTrackClientRentedMovie()
        self.controller.moviesRepository.loadTrackRentedMovies()

        # Load Menu and Submenus
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
                while True:
                    self.refreshScreen()
                    self.rmvSubMenu()
                    option = self.userInput()

                    if option == "1":
                        self.removeMovies()
                    elif option == "2":
                        self.removeClient()
                    elif option == "3":
                        break

            elif option == "3":
                while True:
                    self.refreshScreen()
                    self.updSubMenu()
                    option = self.userInput()

                    if option == "1":
                        self.updateMovies()
                    elif option == "2":
                        self.updateClients()
                    elif option == "3":
                        break

            elif option == "4":
                while True:
                    self.refreshScreen()
                    self.findingSubMenu()
                    option = self.userInput()

                    if option == "1":
                        self.searchMovies()
                    elif option == "2":
                        self.searchClients()
                    elif option == "3":
                        break

            elif option == "5":
                self.rentMovies()

            elif option == "6":
                self.returnMovies()

            elif option == "7":
                while True:
                    self.refreshScreen()
                    self.reportSubMenu()
                    option = self.userInput()

                    if option == "1":
                        self.displayClientsInOrder()
                    elif option == "2":
                        self.displayMostRentedMovies()
                    elif option == "3":
                        self.displayClientsWithMostMovies()
                    elif option == "4":
                        break

            elif option == "8":
                # Save statistics before closing the app.
                self.controller.clientsRepository.saveTrackClientRentedMovies()
                self.controller.moviesRepository.saveTrackRentedMovies()
                break
