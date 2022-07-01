from entity import Expense


class Controller:
    def __init__(self, memory):
        self.memory = memory

    def expense_list(self):
        return self.memory.get_all()

    def adding_expenses(self, data_collected):
        if Expense.check_all_data(data_collected):
            self.memory.save_it(data_collected.__repr__())
        else:
            print("Please try to input your data again!")
