import itertools

from domain.validator import ValidatorError


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
        if movie.title in self.movies_repo.get_names():
            raise ControllerError(f"{movie.title} already exists in repository.")

        try:
            self.validate_movie.validator(movie)
        except ValidatorError as e:
            raise ControllerError(str(e))
        else:
            self.movies_repo.save(movie)

    def add_client(self, client):
        if client.name in self.clients_repo.get_names():
            raise ControllerError(f"{client.name} exists in repository.")

        try:
            self.validate_client.validator(client)
        except ValidatorError as e:
            raise ControllerError(str(e))
        else:
            self.clients_repo.save(client)

    # REMOVE SECTION
    def remove_movie(self, unique_id: int):
        if unique_id not in self.movies_repo.get_id_list():
            raise ControllerError(f"The id: {unique_id}, is not in repository")
        else:
            self.movies_repo.remove(unique_id)

    def remove_clients(self, unique_id: int):
        if unique_id not in self.clients_repo.get_id_list():
            raise ControllerError(f"The id: {unique_id}, is not in repository")
        else:
            self.clients_repo.remove(unique_id)

    # UPDATE SECTION
    def update_movie(self, unique_id: int, new_movie):
        if unique_id not in self.movies_repo.get_id_list():
            raise ControllerError(f'Movie with id {unique_id} does not exist in repository')

        try:
            self.validate_movie.validator(new_movie)
        except ValidatorError as ex:
            raise ControllerError(str(ex))

        return self.movies_repo.update(unique_id, new_movie)

    def update_client(self, unique_id: int, new_client):
        if unique_id not in self.clients_repo.get_id_list():
            raise ControllerError(f"Client with id: {unique_id}, does not exit in repository")

        try:
            self.validate_client.validator(new_client)
        except ValidatorError as e:
            raise ControllerError(str(e))

        return self.clients_repo.update(unique_id, new_client)

    # SEARCH SECTION
    def search_movie(self, find_movie):
        if find_movie in self.movies_repo.get_names():
            return True

    def search_client(self, find_client):
        if find_client in self.clients_repo.get_names():
            return True

    # RENT SECTION
    def rent_movies(self, the_client, the_movie):
        if the_client not in self.clients_repo.get_names():
            raise ControllerError(f"{the_client} is not in repository")

        if the_movie not in self.movies_repo.get_names():
            raise ControllerError(f"{the_movie} is not in repository")

        if not self.validate_movie.check_availability(self.movies_repo.get_movie(the_movie).availability):
            raise ControllerError(f"{the_movie} is not available for rent")

        self.clients_repo.save_movie(the_client, self.movies_repo.get_movie(the_movie).title)
        self.movies_repo.update_status(self.movies_repo.get_movie(the_movie))
        self.movies_repo.add_count(the_movie), self.clients_repo.add_count(the_client)

    # RETURN SECTION
    def return_movies(self, the_client, the_movie):
        if the_client not in self.clients_repo.get_names():
            raise ControllerError(f"{the_client} is not in repository")

        if the_movie not in self.movies_repo.get_names():
            raise ControllerError(f"{the_movie} is not in repository")

        if the_movie not in self.clients_repo.get_rented_movies(the_client):
            raise ControllerError(f"{the_movie} is not rented by {the_client}")

        if self.validate_movie.check_availability(self.movies_repo.get_movie(the_movie).availability):
            raise ControllerError(f"{the_movie} is not rented")

        self.clients_repo.remove_movie(self.movies_repo.get_movie(the_movie).title)
        self.movies_repo.update_status(self.movies_repo.get_movie(the_movie))

    # REPORT SECTION
    # DISPLAY THE CLIENTS THAT HAVE MOVIES IN ALPHABETICAL ORDER
    def display_clients_in_order(self):
        clients_with_movies = []
        for client in self.clients_repo.get_all():
            if self.validate_client.movies_rented(client):
                clients_with_movies.append(client.name)

        clients = sorted(clients_with_movies)
        return clients

    # DISPLAY THE MOST RENTED MOVIE
    def display_most_rented_movie(self):
        values = [count for movie, count in self.movies_repo.track_rented_movies.items()]
        if max(values, default=0) != 0:
            for movie, count in self.movies_repo.track_rented_movies.items():
                if count == max(values):
                    return movie
        else:
            return None

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
        return top30
