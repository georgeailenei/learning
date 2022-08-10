from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def save(self, item):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get(self):
        pass

    def load_tracked_clients_movies(self):
        pass

    def load_tracked_movies(self):
        pass

    def save_tracked_clients_movies(self):
        pass

    def save_tracked_movies(self):
        pass

    def save_all(self, items):
        self.current_id = 1
        for movie in items:
            self.save(movie)
        return self.database

    def remove(self, ID):
        update_repo = [item for item in self.database if ID not in item.__repr__()]
        self.remove_all()
        self.save_all(update_repo)

    def remove_all(self):
        return self.database.clear()

    def get_all(self):
        return self.database

    def get_id_list(self):
        id_list = [item.id for item in self.database]
        return id_list
