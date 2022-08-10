import itertools


class ControllerError(Exception):
    pass


class Controller:
    def __init__(self, movies_repo, clients_repo, validate_movie, validate_client):
        self.movies_repo = movies_repo
        self.clients_repo = clients_repo
        self.validate_movie = validate_movie
        self.validate_client = validate_client

    # ADD SECTION
    def add_movie(self, movie):
        if self.validate_movie.validator(movie):
            self.movies_repo.save(movie)
            return True
        else:
            return False

    def add_client(self, client):
        if self.validate_client.validator(client):
            self.clients_repo.save(client)
            return True
        else:
            return False
    #
    # # REMOVE SECTION
    # def remove_movie(self, unique_id):
    #     if unique_id in self.movies_repo.get_id_list():
    #         self.movies_repo.remove(unique_id)
    #         return True
    #     else:
    #         return False
    #
    # def remove_clients(self, unique_id):
    #     if unique_id in self.clients_repo.get_id_list():
    #         self.clients_repo.remove(unique_id)
    #         return True
    #     else:
    #         return False
    #
    # # UPDATE SECTION
    # def update_movie(self, unique_id, new_movie):
    #     if self.validate_movie.check_id(unique_id):
    #         if unique_id in self.movies_repo.get_id_list():
    #             self.movies_repo.update(unique_id, new_movie)
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

    # def update_client(self, unique_id, new_client):
    #     if self.validate_movie.check_id(unique_id, self.clients_repo.get_id_list()):
    #         self.clients_repo.update(unique_id, new_client)
    #         return True
    #     else:
    #         return False
    #         print(f"\nThe ID: {unique_id} is invalid! Please try again.")

    # # SEARCH SECTION
    # def search_movie(self, find_movie):
    #     if find_movie in self.movies_repo.get_names():
    #         return True
    #
    # def search_client(self, find_client):
    #     if find_client in self.clients_repo.get_names():
    #         return True
    #
    # # RENT SECTION
    # def rent_movies(self, the_client, the_movie):
    #     if the_client in self.clients_repo.get_names():
    #         if the_movie in self.movies_repo.get_names():
    #             if self.validate_movie.check_availability(self.movies_repo.get_movie(the_movie).availability):
    #                 self.clients_repo.save_movie(the_client, self.movies_repo.get_movie(the_movie).title)
    #                 self.movies_repo.update_status(self.movies_repo.get_movie(the_movie))
    #                 self.movies_repo.add_count(the_movie), self.clients_repo.add_count(the_client)
    #             else:
    #                 print(f"\n{the_movie} is not available")
    #         else:
    #             print(f"\nWe do not have {the_movie} in our store.")
    #     else:
    #         print(f"\n{the_client} is not in the client list.")
    #
    # # RETURN SECTION
    # def return_movies(self, the_client, the_movie):
    #     if the_client in self.clients_repo.get_names():
    #         if the_movie in self.movies_repo.get_names():
    #             if the_movie in self.clients_repo.get_client(the_client).rented_movies:
    #                 self.clients_repo.remove_movie(self.movies_repo.get_movie(the_movie).title)
    #                 self.movies_repo.update_status(self.movies_repo.get_movie(the_movie))
    #                 print(f"\nThank Mr.{the_client} for returning the movie: {the_movie}")
    #             else:
    #                 print(f"\n{the_movie} is not rented by {the_client}")
    #         else:
    #             print(f"\nWe do not have {the_movie} in our store.")
    #     else:
    #         print(f"\n{the_client} is not in the client list.")
    #
    # # REPORT SECTION
    # # DISPLAY THE CLIENTS THAT HAVE MOVIES IN ALPHABETICAL ORDER
    # def display_clients_in_order(self):
    #     clients_with_movies = []
    #     for client in self.clients_repo.get_all():
    #         if self.validate_client.movies_rented(client):
    #             clients_with_movies.append(client.name)
    #
    #     clients = sorted(clients_with_movies)
    #     if len(clients_with_movies) == 0:
    #         print("NONE OF THE MOVIES ARE RENTED")
    #     else:
    #         for client in clients:
    #             print(client + " has " + str(self.clients_repo.get_movie_count(client)) + " movie/s")
    #
    # # DISPLAY THE MOST RENTED MOVIE
    # def display_most_rented_movies(self):
    #     values = [count for movie, count in self.movies_repo.track_rented_movies.items()]
    #     if max(values, default=0) != 0:
    #         for movie, count in self.movies_repo.track_rented_movies.items():
    #             if count == max(values):
    #                 print(movie)
    #     else:
    #         print("NONE OF THE MOVIES")
    #
    # # DISPLAY TOP 30% CLIENTS
    # def display_clients_with_most_movies(self):
    #     values = [count for count in self.clients_repo.track_clients_movies.values()]
    #     keys = [name for name in self.clients_repo.track_clients_movies.keys()]
    #     clients = self.clients_repo.track_clients_movies
    #     values.sort(), values.reverse()
    #
    #     clients_in_order = {}
    #     check = 0
    #     value_checker = 0
    #
    #     while len(values) > check:
    #         if values[check] == clients[keys[value_checker]]:
    #             clients_in_order[keys[value_checker]] = values[check]
    #             check += 1
    #             value_checker = 0
    #         else:
    #             value_checker += 1
    #
    #     x = (len(clients_in_order) * 30) / 100
    #     top30 = dict(itertools.islice(clients_in_order.items(), round(x)))
    #
    #     if len(top30) == 0:
    #         print("NONE OF THE CLIENTS")
    #
    #     return top30
