import copy
from abc import ABC, abstractmethod
from copy import deepcopy


class RepositoryError(Exception):
    pass


class ExpenseRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def save(self, expense):
        pass

    @abstractmethod
    def save_all(self, expenses):
        pass

    @abstractmethod
    def remove(self, ex):
        pass

    @abstractmethod
    def remove_all(self):
        pass

    @abstractmethod
    def get(self, expense_id):
        pass

    @abstractmethod
    def update(self, expense):
        pass


class InMemoryRepository(ExpenseRepository, ABC):
    def __init__(self):
        self.expenses = []
        self.current_id = 1

    def save(self, expense):
        expense.id = self.current_id
        self.expenses.append(expense)
        self.current_id += 1

    def remove(self, requested_format):
        update_expense_list = []

        for expense in self.expenses:
            expense = expense.split()
            if requested_format not in expense:
                expense = " ".join(expense)
                update_expense_list.append(expense)
        return update_expense_list

    def get_all(self):
        return self.expenses

    def save_all(self, expenses):
        for expense in expenses:
            self.save(expense)
        return self.expenses

    def remove_all(self):
        return self.expenses.clear()

    def get(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return deepcopy(expense)
        return None

    def update(self, to_update_expense):
        for expense in self.expenses:
            if expense.id == to_update_expense.id:
                expense.date = to_update_expense.date
                expense.amount = to_update_expense.amount
                expense.expense_type = to_update_expense.expense_type
                return
        raise RepositoryError(f'Expense with id {to_update_expense.id} does not exist')

    def timeline(self):
        timeline = [[]]
        lastExpenseList = -1

        if self.expenses not in timeline[lastExpenseList]:
            timeline.append([])
            # for expense in self.expenses:
            #     timeline[lastExpenseList].append(copy.deepcopy(expense))
        return timeline

    def redo(self):
        pass
