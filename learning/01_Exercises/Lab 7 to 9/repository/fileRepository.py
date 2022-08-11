from domain.entity import Client, Movie
from abc import ABC, abstractmethod


class RepositoryError(Exception):
    pass


class FileRepository(ABC):
    @abstractmethod
    def update(self, unique_id, item):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_names(self):
        pass

    @abstractmethod
    def save(self, item):
        pass

    def save_all(self, items):
        for item in items:
            self.save(item)

    def remove(self, unique_id: int):
        update_repo = [item for item in self.get_all() if unique_id != int(item.id)]
        self.remove_all()
        self.save_all(update_repo)

    def remove_all(self):
        file = open(self.file_name, "w")
        file.close()

    def get_id_list(self):
        id_list = [int(item.id) for item in self.get_all()]
        return id_list


class ClientFileRepository(FileRepository):
    def __init__(self):
        self.file_name = "repository/clients.text"
        self.track_clients_movies = {}
        self.rented_movies = ""
        self.current_count = 0
        self.current_id = 1

    def load_tracked_clients_movies(self):
        with open("repository/Track_Client_Rented_Movie.text", "r") as f:
            lines = f.readlines()

            for line in lines:
                static = line.split(":")
                self.track_clients_movies[static[0].strip()] = int(static[1].strip())

    def save_tracked_clients_movies(self):
        with open("repository/Track_Client_Rented_Movie.text", "w") as file:
            for key, value in self.track_clients_movies.items():
                file.write(key + ": ")
                file.write(str(value) + "\n")

    def add_count(self, theClient):
        self.track_clients_movies[theClient] += 1

    def get_all(self):
        file = open(self.file_name, "r")

        lines = file.readlines()
        if len(lines) == 0:
            return []
        else:
            clients_list = []
            unique_id, name, cnp, rented_movies = 0, 1, 2, 3

            for info in lines:
                info = info.split(":")
                client_info = Client(info[name].strip(), info[cnp].strip())
                client_info.id = info[unique_id].strip()
                client_info.rented_movies = info[rented_movies].strip()
                clients_list.append(client_info)
            return clients_list

    def save(self, client_info):
        with open(self.file_name, "a") as file:
            if len(self.get_all()) == 0:
                client_info.id = self.current_id
            else:
                client_info.id = int(self.get_all()[-1].id) + 1

            if len(self.rented_movies) < len(client_info.rented_movies):
                pass
            else:
                client_info.rented_movies = self.rented_movies
            if client_info.name not in self.track_clients_movies:
                self.track_clients_movies[client_info.name] = self.current_count
            file.write(str(client_info) + "\n")

    def update(self, unique_id, new_client):
        updated_list = []
        for client_info in self.get_all():
            if unique_id == int(client_info.id):
                client_info.name = new_client.name
                client_info.CNP = new_client.CNP
                client_info.rented_movies = new_client.rented_movies
                updated_list.append(client_info)
            else:
                updated_list.append(client_info)
        self.remove_all()
        self.save_all(updated_list)

    def save_movie(self, the_client, the_movie):
        for client_info in self.get_all():
            if the_client == client_info.name:
                client_info.rented_movies = client_info.rented_movies + " " + the_movie + ";"
                self.update(int(client_info.id), client_info)

    def remove_movie(self, the_movie):
        for client_info in self.get_all():
            if the_movie in client_info.rented_movies:
                movie_list = str(client_info.rented_movies).split(";")
                movie_list = [name.strip() for name in movie_list]
                movie_list.remove(the_movie)
                client_info.rented_movies = "; ".join(movie_list)
                self.update(int(client_info.id), client_info)

    def get_names(self):
        client_names = [client_info.name for client_info in self.get_all()]
        return client_names

    def get_client(self, the_client):
        for client_info in self.get_all():
            if the_client == client_info.name:
                return client_info

    def get_id(self, the_client):
        for client_info in self.get_all():
            if client_info.name == the_client:
                return client_info.id

    def get_movie_count(self, the_client):
        for client_info in self.get_all():
            if client_info.name == the_client:
                movie_list = str(client_info.rented_movies).split(";")
                count = len(movie_list) - 1
                return count

    def get_rented_movies(self, the_client):
        client = self.get_client(the_client)
        return client.rented_movies


class MoviesFileRepository(FileRepository):
    def __init__(self, file_name):
        self.file_name = file_name
        self.current_availability = "Available"
        self.track_rented_movies = {}
        self.current_id = 1

    def load_tracked_movies(self):
        with open("repository/Track_Rented_Movies.text", "r") as f:
            lines = f.readlines()

            for line in lines:
                statistic = line.split(":")
                self.track_rented_movies[statistic[0].strip()] = int(statistic[1].strip())

    def save_tracked_movies(self):
        with open("repository/Track_Rented_Movies.text", "w") as file:
            for key, value in self.track_rented_movies.items():
                file.write(key + ": ")
                file.write(str(value) + "\n")

    def add_count(self, theMovie):
        self.track_rented_movies[theMovie] += 1

    def get_all(self):
        file = open(self.file_name, "r")

        lines = file.readlines()
        if len(lines) == 0:
            return []
        else:
            movie_list = []
            unique_id, title, description, genre, availability = 0, 1, 2, 3, 4

            for info in lines:
                info = info.split(":")
                movie_info = Movie(info[title].strip(), info[description].strip(), info[genre].strip())
                movie_info.id = int(info[unique_id].strip())
                movie_info.availability = info[availability].strip()
                movie_list.append(movie_info)
            return movie_list

    def save(self, movie_info):
        with open(self.file_name, "a") as file:
            if len(self.get_all()) == 0:
                movie_info.id = self.current_id
            else:
                movie_info.id = int(self.get_all()[-1].id) + 1

            if len(self.current_availability) < len(str(movie_info.availability)):
                pass
            else:
                movie_info.availability = self.current_availability

            if movie_info.title not in self.track_rented_movies:
                self.track_rented_movies[movie_info.title] = 0
            file.write(str(movie_info) + "\n")

    def update(self, unique_id, new_movie):
        updated_list = []
        updated_movie = False
        for movie_info in self.get_all():
            if unique_id == int(movie_info.id):
                updated_movie = True
                movie_info.title = new_movie.title
                movie_info.description = new_movie.description
                movie_info.genre = new_movie.genre
                movie_info.availability = new_movie.availability
                updated_list.append(movie_info)
            else:
                updated_list.append(movie_info)

        if updated_movie is False:
            raise RepositoryError(f'Movie with id {unique_id} does not exist')

        self.remove_all()
        self.save_all(updated_list)

    def get_movie(self, the_movie):
        for movie_info in self.get_all():
            if the_movie == movie_info.title:
                return movie_info

    def get_names(self):
        movie_names = [movie_info.title for movie_info in self.get_all()]
        return movie_names

    def get_id(self, the_movie):
        for movie_info in self.get_all():
            if movie_info.title == the_movie:
                return movie_info.id

    def update_status(self, the_movie):
        if the_movie.availability == "Available":
            the_movie.availability = "NOT AVAILABLE"
            self.update(self.get_id(the_movie.title), the_movie)
        elif the_movie.availability == "NOT AVAILABLE":
            the_movie.availability = "Available"
            self.update(self.get_id(the_movie.title), the_movie)
