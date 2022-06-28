from repository import Repository
from entity import Expense


class ConsoleRepository(Repository):
    def __init__(self):
        self.expenses = []

    def save(self, expense):
        self.expenses.append(expense)

    def remove_all(self):
        return self.expenses.clear()

    def get_all_expenses(self):
        return self.expenses

    def add_to_repository(self, expenses):
        for expense in expenses:
            console_memory.save(expense)
        return self.expenses


class Remove:
    def __init__(self, expenses, requested_format):
        self.expenses = expenses
        self.requested_format = requested_format

    def remove(self):
        """The function takes expense list and remove the expenses depending on the requested format
        It returns a new list of expense"""
        expenses = []

        for expense in self.expenses:
            expense = expense.split()
            if self.requested_format not in expense:
                expense = " ".join(expense)
                expenses.append(expense)
        return expenses


console_memory = ConsoleRepository()
repository = console_memory.get_all_expenses()
console_memory.save(Expense("23-04-2020", "10", "Other").__repr__())
console_memory.save(Expense("25-04-2020", "20", "Phone").__repr__())
console_memory.save(Expense("27-04-2020", "350", "Bills").__repr__())
console_memory.save(Expense("23-04-2020", "10", "Other").__repr__())
