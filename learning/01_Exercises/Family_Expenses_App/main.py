from interface import ConsoleUI
from repository import InMemoryRepository
from control import Controller
from entity import ExpenseValidator, Expense


def main():
    validator = ExpenseValidator()
    repository = InMemoryRepository()
    controller = Controller(repository, validator)
    controller.add_expense(Expense('01-11-96', '100', 'Food'))
    user_interface = ConsoleUI(controller)
    user_interface.start()


if __name__ == "__main__":
    main()
