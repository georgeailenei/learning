from domain.entity import Movie, Client
import os


class Ui:
    main_title = "This app manages movies and clients for Company X"
    menu = '1. Add\n' \
           '2. Remove\n' \
           '3. Update\n' \
           '4. Search\n' \
           '5. Rent\n' \
           '6. Returns\n' \
           '7. Reports\n' \
           '8. Exit'

    sub_menu_add = "1. Add movies\n" \
                   "2. Add clients\n" \
                   "3. Return to Main Menu"

    sub_menu_remove = "1. Remove movies\n" \
                      "2. Remove clients\n" \
                      "3. Return to Main Menu"

    sub_menu_update = "1. Update movies\n" \
                      "2. Update clients\n" \
                      "3. Return to Main Menu"

    sub_menu_search = "1. Search for movies\n" \
                      "2. Search for clients\n" \
                      "3. Return to Main Menu"

    sub_menu_reports = "1. Display clients\n" \
                       "2. Display most rented movies\n" \
                       "3. Display top 3 clients with most rented movies\n" \
                       "4. Return to Main Menu"

    def __init__(self, controller):
        self.controller = controller

    def user_input(self):
        option = input("Choose option: ")
        return option

    def main_menu(self):
        print(self.main_title)
        print(self.menu)

    def add_sub_menu(self):
        print(self.sub_menu_add)

    def remove_sub_menu(self):
        print(self.sub_menu_remove)

    def update_sub_menu(self):
        print(self.sub_menu_update)

    def search_sub_menu(self):
        print(self.sub_menu_search)

    def reports_sub_menu(self):
        print(self.sub_menu_reports)

    def exit(self):
        option = input("Do you want to continue (N/Y): ")
        if option == "N":
            return False
        elif option == "Y":
            return True

    def refresh_screen(self):
        return os.system("cls")

    def collect_word(self):
        word = input("Search: ")
        return word

    def collect_id(self):
        print("\nPlease insert an ID")
        unique_id = input("Write ID: ")
        return unique_id

    def collect_movie_data(self):
        print("\nPlease insert the following information")
        title = input("Movie title: ")
        description = input("Description: ")
        genre = input("Genre: ")
        return Movie(title, description, genre)

    def collect_client_data(self):
        print("\nPlease insert the following information")
        name = input("Name: ")
        cnp = input("CNP: ")
        return Client(name, cnp)

    def display_movies(self):
        print("This is the current list with movies")
        all_movies = self.controller.moviesRepository.get_all()
        if len(all_movies) == 0:
            print("- no movies")
        else:
            for the_movie in all_movies:
                print(the_movie)

    def display_clients(self):
        print("This is the current list with clients")
        all_clients = self.controller.clientsRepository.get_all()
        if len(all_clients) == 0:
            print("- no clients info")
        for client_info in all_clients:
            print(client_info)

    def display_movie_count(self):
        print("The current count for each movie")
        for the_movie, the_count in self.controller.moviesRepository.track_rented_movies.items():
            print(the_movie, the_count)

    def display_clients_movie_count(self):
        print("The current list with clients and their rented movie count")
        for the_client, the_count in self.controller.clientsRepository.track_clients_movies.items():
            print(the_client, the_count)

    def display_top30_clients(self, clients):
        for client, count in clients.items():
            print(client, count)

    def add_movie(self):
        while True:
            self.refresh_screen()
            print("ADD MOVIES")

            self.display_movies()
            new_movie = self.collect_movie_data()
            self.controller.add_movie(new_movie)
            if not self.exit():
                break

    def add_client(self):
        while True:
            self.refresh_screen()
            print("ADD CLIENTS")

            self.display_clients()
            client = self.collect_client_data()
            self.controller.add_client(client)
            if not self.exit():
                break

    def remove_movie(self):
        while True:
            self.refresh_screen()
            print("REMOVE MOVIES")

            self.display_movies()
            unique_id = self.collect_id()
            self.controller.remove_movie(unique_id)
            if not self.exit():
                break

    def remove_client(self):
        while True:
            self.refresh_screen()
            print("REMOVE CLIENTS")
            self.display_clients()

            unique_id = self.collect_id()
            self.controller.remove_clients(unique_id)
            if not self.exit():
                break

    def update_movie(self):
        while True:
            self.refresh_screen()
            print("UPDATE MOVIES")
            self.display_movies()

            # Collect the movie unique_id.
            unique_id = self.collect_id()
            if not self.controller.validatorForMovie.check_id(unique_id, self.controller.moviesRepository.get_id_list()):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Collect new data to update the list.
            newMovie = self.collect_movie_data()
            if not self.controller.validatorForMovie.validator(newMovie, self.controller.moviesRepository.get_names()):
                # You must raise an error/message for the user to know what's going on.
                continue

            self.controller.update_movie(unique_id, newMovie)
            if not self.exit():
                break

    def update_clients(self):
        while True:
            self.refresh_screen()
            print("UPDATE CLIENTS")
            self.display_clients()

            # Collect the client's unique_id.
            unique_id = self.collect_id()
            if not self.controller.validatorForClient.check_id(unique_id, self.controller.clientsRepository.get_id_list()):
                # You must raise an error/message for the user to know what's going on.
                continue

            # Collect new data to update the list.
            new_client = self.collect_client_data()
            if not self.controller.validatorForClient.validator(new_client, self.controller.clientsRepository.get_names()):
                # You must raise an error/message for the user to know what's going on.
                continue

            self.controller.update_client(unique_id, new_client)
            if not self.exit():
                break

    def search_movies(self):
        while True:
            self.refresh_screen()
            print("SEARCH FOR MOVIES")

            find_movie = self.collect_word()
            self.controller.search_movie(find_movie)
            if not self.exit():
                break

    def search_clients(self):
        while True:
            self.refresh_screen()
            print("SEARCH FOR CLIENTS")

            find_client = self.collect_word()
            self.controller.search_client(find_client)
            if not self.exit():
                break

    def rent_movies(self):
        while True:
            self.refresh_screen()

            print("RENT MOVIES")
            self.display_movies()

            print("\nTHE CLIENT LIST")
            self.display_clients()

            the_client = input("Choose a client: ")
            the_movie = input("Choose a movie: ")
            self.controller.rent_movies(the_client, the_movie)
            if not self.exit():
                break

    def return_movies(self):
        while True:
            self.refresh_screen()
            print("RETURN MOVIES")
            self.display_movies()

            print("\nTHE CLIENT LIST")
            self.display_clients()

            the_client = input("Choose a client: ")
            the_movie = input("Choose a movie: ")

            self.controller.return_movies(the_client, the_movie)
            if not self.exit():
                break

    def display_clients_in_order(self):
        while True:
            self.refresh_screen()
            print("DISPLAY CLIENTS WITH MOVIES")

            self.controller.display_clients_in_order()
            if not self.exit():
                break

    def display_most_rented_movies(self):
        while True:
            self.refresh_screen()
            self.display_movie_count()

            print("\nMost rented movie: ")
            self.controller.display_most_rented_movies()
            if not self.exit():
                break

    def display_clients_with_most_movies(self):
        while True:
            self.refresh_screen()
            self.display_clients_movie_count()

            print("\nTOP 30% clients are: ")
            top30 = self.controller.display_clients_with_most_movies()
            self.display_top30_clients(top30)
            if not self.exit():
                break

    def run(self):
        # Load Statistics
        self.controller.clientsRepository.load_tracked_clients_movies()
        self.controller.moviesRepository.load_tracked_movies()

        # Load Menu and Submenus
        while True:
            self.refresh_screen()
            self.main_menu()
            option = self.user_input()

            if option == "1":
                while True:
                    self.refresh_screen()
                    self.add_sub_menu()
                    option = self.user_input()

                    if option == "1":
                        self.add_movie()
                    elif option == "2":
                        self.add_client()
                    elif option == "3":
                        break

            elif option == "2":
                while True:
                    self.refresh_screen()
                    self.remove_sub_menu()
                    option = self.user_input()

                    if option == "1":
                        self.remove_movie()
                    elif option == "2":
                        self.remove_client()
                    elif option == "3":
                        break

            elif option == "3":
                while True:
                    self.refresh_screen()
                    self.update_sub_menu()
                    option = self.user_input()

                    if option == "1":
                        self.update_movie()
                    elif option == "2":
                        self.update_clients()
                    elif option == "3":
                        break

            elif option == "4":
                while True:
                    self.refresh_screen()
                    self.search_sub_menu()
                    option = self.user_input()

                    if option == "1":
                        self.search_movies()
                    elif option == "2":
                        self.search_clients()
                    elif option == "3":
                        break

            elif option == "5":
                self.rent_movies()

            elif option == "6":
                self.return_movies()

            elif option == "7":
                while True:
                    self.refresh_screen()
                    self.reports_sub_menu()
                    option = self.user_input()

                    if option == "1":
                        self.display_clients_in_order()
                    elif option == "2":
                        self.display_most_rented_movies()
                    elif option == "3":
                        self.display_clients_with_most_movies()
                    elif option == "4":
                        break

            elif option == "8":
                # Save statistics before closing the app.
                self.controller.clientsRepository.save_tracked_clients_movies()
                self.controller.moviesRepository.save_tracked_movies()
                break
