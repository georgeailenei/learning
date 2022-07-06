from interface import ConsoleUI
from repository import InMemoryRepository
from control import Controller
from entity import ExpenseValidator


def main():
    validator = ExpenseValidator()
    repository = InMemoryRepository()
    controller = Controller(repository, validator)
    user_interface = ConsoleUI(controller)
    user_interface.start()


if __name__ == "__main__":
    main()
