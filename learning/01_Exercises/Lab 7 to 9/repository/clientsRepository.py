from repository.repository import Repository


class ClientsRepository(Repository):
    def __init__(self):
        self.database = []
        self.current_id = 1
        self.track_clients_movies = {}
        self.rented_movies = ""
        self.current_count = 0

    def get(self):
        pass

    # Tested
    def save(self, client: object):
        client.id = self.current_id
        self.database.append(client)
        self.track_clients_movies[client.name] = self.current_count
        self.current_id += 1

    # Tested
    def add_count(self, client: str):
        self.track_clients_movies[client] += 1

    # Tested
    def update(self, unique_id: str, new_client: object):
        updated_database = []
        for client in self.database:
            if unique_id in str(client.id):
                client.name = new_client.name
                client.CNP = new_client.CNP
                updated_database.append(client)
            else:
                updated_database.append(client)
        self.remove_all()
        self.save_all(updated_database)

    # Tested
    def get_names(self):
        name_list = [client.name for client in self.database]
        return name_list

    # Tested
    def get_client(self, the_client: str):
        for client in self.get_all():
            if the_client == client.name:
                return client

    # Tested
    def save_movie(self, the_client: str, movie: str):
        for client in self.database:
            if the_client == client.name:
                client.rented_movies = client.rented_movies + " " + movie + ";"

    # Tested
    def remove_movie(self, movie: str):
        for client in self.database:
            if movie in client.rented_movies:
                movie_list = str(client.rented_movies).split(";")
                movie_list = [name.strip() for name in movie_list]
                movie_list.remove(movie)
                client.rented_movies = "; ".join(movie_list)

    # Tested
    def get_movie_count(self, the_client: str):
        for client in self.get_all():
            if client.name == the_client:
                movie_list = str(client.rented_movies).split(";")
                count = len(movie_list) - 1
                return count
