import itertools


class ControllerError(Exception):
    pass


class Controller:
    def __init__(self, movies_repository, clients_repository, movie_validator, client_validator):
        self.movies_repo = movies_repository
        self.clients_repo = clients_repository
        self.validate_movie = movie_validator
        self.validate_client = client_validator

    # ADD SECTION
    def add_movie(self, movie):
        if self.validate_movie.validator(movie, self.movies_repo.get_names()):
            self.movies_repo.save(movie)
            print(f"\n{movie} has been added to the list.")
        else:
            print(f"The {movie} contains some wrong information")

    def add_client(self, client):
        if self.validate_client.validator(client, self.clients_repo.get_names()):
            self.clients_repo.save(client)
            print(f"\n{client} has been added to the list.")
        else:
            print(f"The {client}'s details appears to be wrong, please try again.")

    # REMOVE SECTION
    def remove_movie(self, unique_id):
        if unique_id in self.movies_repo.get_id_list():
            new_movie_list = self.movies_repo.remove(unique_id)
            self.movies_repo.remove_all()
            self.movies_repo.save_all(new_movie_list)
            print(f"\nThe movie with {unique_id} id has been removed.")
        else:
            print(f"\nThe ID: {unique_id} is invalid! Please try again.")

    def remove_clients(self, unique_id):
        if unique_id in self.clients_repo.get_id_list():
            new_client_list = self.clients_repo.remove(unique_id)
            self.clients_repo.remove_all()
            self.clients_repo.save_all(new_client_list)
            print(f"\nThe client with {unique_id} id has been removed.")
        else:
            print(f"\nThe ID: {unique_id} is invalid! Please try again.")

    # UPDATE SECTION
    def update_movie(self, unique_id, new_movie):
        if self.validate_movie.check_id(unique_id, self.movies_repo.get_id_list()):
            self.movies_repo.update(unique_id, new_movie)
        else:
            print(f"\nThe ID: {unique_id} is invalid! Please try again.")

    def update_client(self, unique_id, new_client):
        if self.validate_movie.check_id(unique_id, self.clients_repo.get_id_list()):
            self.clients_repo.update(unique_id, new_client)
        else:
            print(f"\nThe ID: {unique_id} is invalid! Please try again.")

    # SEARCH SECTION
    def search_movie(self, find_movie):
        if find_movie in self.movies_repo.get_names():
            for movie in self.movies_repo.get_all():
                if movie.title == find_movie:
                    print(f"{find_movie} | Found! | Full information: ")
                    print(f"{movie}")
        else:
            print(f"{find_movie} | Could not been found! Please try again.")

    def search_client(self, find_client):
        if find_client in self.clients_repo.get_names():
            for client in self.clients_repo.get_all():
                if client.name == find_client:
                    print(f"{find_client} | Found! | Full information: ")
                    print(f"{client}")
        else:
            print(f"{find_client} | Could not been found! Please try again.")

    # RENT SECTION
    def rent_movies(self, the_client, the_movie):
        if the_client in self.clients_repo.get_names():
            if the_movie in self.movies_repo.get_names():
                if self.validate_movie.check_availability(self.movies_repo.get_movie(the_movie).availability):
                    self.clients_repo.save_movie(the_client, self.movies_repo.get_movie(the_movie).title)
                    self.movies_repo.update_status(self.movies_repo.get_movie(the_movie))
                    self.movies_repo.add_count(the_movie), self.clients_repo.add_count(the_client)
                else:
                    print(f"\n{the_movie} is not available")
            else:
                print(f"\nWe do not have {the_movie} in our store.")
        else:
            print(f"\n{the_client} is not in the client list.")

    # RETURN SECTION
    def return_movies(self, the_client, the_movie):
        if the_client in self.clients_repo.get_names():
            if the_movie in self.movies_repo.get_names():
                if the_movie in self.clients_repo.get_client(the_client).rented_movies:
                    self.clients_repo.remove_movie(self.movies_repo.get_movie(the_movie).title)
                    self.movies_repo.update_status(self.movies_repo.get_movie(the_movie))
                    print(f"\nThank Mr.{the_client} for returning the movie: {the_movie}")
                else:
                    print(f"\n{the_movie} is not rented by {the_client}")
            else:
                print(f"\nWe do not have {the_movie} in our store.")
        else:
            print(f"\n{the_client} is not in the client list.")

    # REPORT SECTION
    # DISPLAY THE CLIENTS THAT HAVE MOVIES IN ALPHABETICAL ORDER
    def display_clients_in_order(self):
        clients_with_movies = []
        for client in self.clients_repo.get_all():
            if self.validate_client.movies_rented(client):
                clients_with_movies.append(client.name)

        clients = sorted(clients_with_movies)
        if len(clients_with_movies) == 0:
            print("NONE OF THE MOVIES ARE RENTED")
        else:
            for client in clients:
                print(client + " has " + str(self.clients_repo.get_movie_count(client)) + " movie/s")

    # DISPLAY THE MOST RENTED MOVIE
    def display_most_rented_movies(self):
        values = [count for movie, count in self.movies_repo.track_rented_movies.items()]
        if max(values, default=0) != 0:
            for movie, count in self.movies_repo.track_rented_movies.items():
                if count == max(values):
                    print(movie)
        else:
            print("NONE OF THE MOVIES")

    # DISPLAY TOP 30% CLIENTS
    def display_clients_with_most_movies(self):
        values = [count for count in self.clients_repo.track_clients_movies.values()]
        keys = [name for name in self.clients_repo.track_clients_movies.keys()]
        clients = self.clients_repo.track_clients_movies
        values.sort(), values.reverse()

        clients_in_order = {}
        check = 0
        value_checker = 0

        while len(values) > check:
            if values[check] == clients[keys[value_checker]]:
                clients_in_order[keys[value_checker]] = values[check]
                check += 1
                value_checker = 0
            else:
                value_checker += 1

        x = (len(clients_in_order) * 30) / 100
        top30 = dict(itertools.islice(clients_in_order.items(), round(x)))

        if len(top30) == 0:
            print("NONE OF THE CLIENTS")

        return top30
