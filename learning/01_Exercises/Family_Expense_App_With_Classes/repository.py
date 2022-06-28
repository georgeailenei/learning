from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_all_expenses(self):
        pass

    @abstractmethod
    def save(self):
        pass
