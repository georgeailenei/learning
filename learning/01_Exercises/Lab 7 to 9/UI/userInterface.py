from domain.entity import movie, client
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

    def reportSubMenu(self):
        # It displays the sub menu for Report section.
        print(self.reportsSubMenu)

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
        allMovies = self.controller.moviesRepository.getAll()
        if len(allMovies) == 0:
            print("- no movies")
        else:
            for theMovie in allMovies:
                print(theMovie)

    def displayClients(self):
        # It prints all the movies that are currently in clientRepo.
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
            if not self.controller.validatorForMovie.checkID(ID, self.controller.moviesRepository.getIdList()):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Collect new data to update the list.
            newMovie = self.collectMovieData()
            if not self.controller.validatorForMovie.validator(newMovie, self.controller.moviesRepository.getNames()):
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
            if not self.controller.validatorForClient.checkID(ID, self.controller.clientsRepository.getIdList()):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Collect new data to update the list.
            newClient = self.collectClientsData()
            if not self.controller.validatorForClient.validator(newClient, self.controller.clientsRepository.getNames()):
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

            # Collect the name of the client.
            findClient = self.collectWord()

            # Try to find the client in the client database.
            self.controller.searchClients(findClient)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def rentMovies(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title and the movie list.
            print("RENT MOVIES")
            self.displayMovies()

            # Display the client list.
            print("\nTHE CLIENT LIST")
            self.displayClients()

            # Collect the name of the client and the name of the movie.
            theClient = input("Choose a client: ")
            theMovie = input("Choose a movie: ")

            # Try to attach the movie to the clients - rented movies list.
            self.controller.rentMovies(theClient, theMovie)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def returnMovies(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title and the movie list.
            print("RETURN MOVIES")
            self.displayMovies()

            # Display the client list.
            print("\nTHE CLIENT LIST")
            self.displayClients()

            # Collect the name of the client and the name of the movie.
            theClient = input("Choose a client: ")
            theMovie = input("Choose a movie: ")

            # Try to attach the movie to the clients - rented movies list.
            self.controller.returnMovies(theClient, theMovie)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def displayClientsInOrder(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the title.
            print("THIS IS THE CLIENTS LIST")

            # Try to display the client's list in order.
            self.controller.displayClientsInOrder()

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def displayMostRentedMovies(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the movie count.
            self.displayMoviesCount()

            # Display the most rented movie
            print("\nMost rented movie: ")
            self.controller.displayMostRentedMovies()

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def displayClientsWithMostMovies(self):
        while True:
            # Refresh the screen.
            self.refreshScreen()

            # Display the clients and movie count.
            self.displayClientsMovieCount()

            # Display top 30% clients that hold most movies rented.
            print("\nTOP 30% clients are: ")
            top30 = self.controller.displayClientsWithMostMovies()
            self.displayTop30Clients(top30)

            # Ask the user if he wants to continue
            if not self.exit():
                break

    def run(self):
        # Load Statistics
        self.controller.clientsRepository.loadTrackClientRentedMovie()
        self.controller.moviesRepository.loadTrackRentedMovies()

        # Load Menu and Submenus
        while True:
            self.refreshScreen(), self.mainMenu()
            option = self.userInput()

            if option == "1":
                while True:
                    self.refreshScreen(), self.subMenu()
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

            elif option == "5":
                self.rentMovies()

            elif option == "6":
                self.returnMovies()

            elif option == "7":
                while True:
                    self.refreshScreen(), self.reportSubMenu()
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
