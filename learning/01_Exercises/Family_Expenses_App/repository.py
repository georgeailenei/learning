from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def save(self):
        pass


class Memory(Repository, ABC):
    def __init__(self):
        self.expenses = []

    def save(self):
        pass

    def save_it(self, expense):
        self.expenses.append(expense)

    def remove_it(self, requested_format):
        update_expense_list = []

        for expense in self.expenses:
            expense = expense.split()
            if requested_format not in expense:
                expense = " ".join(expense)
                update_expense_list.append(expense)
        return update_expense_list

    def remove_all(self):
        return self.expenses.clear()

    def get_all(self):
        return self.expenses

    def add_to_repository(self, expenses):
        for expense in expenses:
            self.save_it(expense)
        return self.expenses


memory = Memory()
