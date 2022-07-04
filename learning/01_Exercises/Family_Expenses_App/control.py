from entity import Expense
from repository import repository
from entity_features import MultipleDataFeatures, EntityFeatures


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

    def update_expenses(self, data_collected, updated_expense):
        expense = data_collected.__repr__()
        if expense in self.memory.get_all():
            expense_location = repository.index(expense)
            repository.remove(expense)
            while True:
                new_expense = updated_expense
                update_the_expense = new_expense.__repr__()
                if Expense.check_all_data(updated_expense):
                    repository.insert(expense_location, update_the_expense)
                    break
                else:
                    print("Please try to input your data again!")
        else:
            print("We could not find your expense, try again!\n")

    def remove_expenses_by_date(self, data_collected):
        date = Expense(data_collected, "", "")
        if date.check_date_format():
            update_expenses = self.memory.remove_it(data_collected)
            self.memory.remove_all()
            self.memory.add_to_repository(update_expenses)
        else:
            print("Please write in this format (dd-mm-yy)")

    def remove_expenses_by_type(self, data_collected):
        expense_type = Expense("", "", data_collected)
        if expense_type.check_type():
            update_expenses = self.memory.remove_it(data_collected)
            self.memory.remove_all()
            self.memory.add_to_repository(update_expenses)
        else:
            print("The app does not support that type of expense")

    def remove_expenses_by_time(self, from_date, to_date):
        dates = [Expense(from_date, "", ""), Expense(to_date, "", "")]
        if dates[0].check_date_format() and dates[1].check_date_format():
            if dates[0].check_day_format() and dates[1].check_day_format():
                MultipleDataFeatures(self.memory.get_all(), from_date, to_date).remove_by_time_interval()
        else:
            print("\nPlease try to input a date again.\n")

    def search_higher_expenses(self, data_collected):
        expense = Expense("", data_collected, "")
        if expense.check_amount():
            found_expenses = EntityFeatures(self.memory, data_collected).find_greater_expenses()
            if len(found_expenses) == 0:
                found_expenses.append(f"There aren't bigger numbers than {data_collected}")
                return found_expenses
            else:
                return found_expenses
        else:
            return ["Please insert a number not random things."]


random_expenses = [Expense("23-04-2022", "2", "Other"), Expense("24-04-2022", "5", "Phone"), Expense("23-04-2022", "10", "Other"), Expense("25-04-2022", "15", "Bills")]
print(Controller(random_expenses).search_higher_expenses("2"))
