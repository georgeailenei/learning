from abc import ABC, abstractmethod


class UI(ABC):
    @abstractmethod
    def user_input(self):
        pass
    