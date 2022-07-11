from abc import ABC, abstractmethod


class repository(ABC):

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def remove(self):
        pass
