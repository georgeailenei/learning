from entity_features import MultipleDataFeatures, EntityFeatures, SingleDataFeatures
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

    def check_expense_list(self):
        if len(self.memory.get_all()) == 0:
            return False
        else:
            return True

    def update_expenses(self, data_collected, updated_expense):
        expense = data_collected.__repr__()
        if expense in self.memory.get_all():
            expense_location = self.memory.get_all().index(expense)
            self.memory.get_all().remove(expense)
            while True:
                new_expense = updated_expense
                update_the_expense = new_expense.__repr__()
                if Expense.check_all_data(updated_expense):
                    self.memory.get_all().insert(expense_location, update_the_expense)
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

    def remove_by_time_interval(self, from_date, to_date):
        the_dates = SingleDataFeatures(self.memory.get_all()).get_date()
        the_month = [SingleDataFeatures(self.memory.get_all()).get_month(from_date), SingleDataFeatures(self.memory.get_all()).get_month(to_date)]
        remove_from_day = SingleDataFeatures(self.memory.get_all()).get_day(from_date)
        remove_to_day = SingleDataFeatures(self.memory.get_all()).get_day(to_date)
        update_expenses = []
        i = 0

        if the_month[0] == the_month[1]:
            while len(self.memory.get_all()) > i:
                if remove_from_day <= SingleDataFeatures(self.memory.get_all()).get_day(the_dates[i]) <= remove_to_day:
                    i += 1
                else:
                    update_expenses.append(self.memory.get_all()[i])
                    i += 1
            self.memory.remove_all()
            self.memory.add_to_repository(update_expenses)
        else:
            print("The time interval is too long, please choose same month or subscribe to premium :))")

    def remove_expenses_by_time(self, from_date, to_date):
        dates = [Expense(from_date, "", ""), Expense(to_date, "", "")]
        if dates[0].check_date_format() and dates[1].check_date_format():
            if dates[0].check_day_format() and dates[1].check_day_format():
                self.remove_by_time_interval(from_date, to_date)
        else:
            print("\nPlease try to input a date again.\n")

    def search_higher_expenses(self, data_collected):
        expense = Expense("", data_collected, "")
        if expense.check_amount():
            found_expenses = EntityFeatures(self.memory.get_all(), data_collected).find_greater_expenses()
            if len(found_expenses) == 0:
                found_expenses.append(f"There aren't bigger numbers than {data_collected}")
                return found_expenses
            else:
                return found_expenses
        else:
            return ["Please insert a number not random things."]

    def search_same_type_expenses(self, data_collected):
        expense = Expense("", "", data_collected)
        if expense.check_type():
            expenses_found = EntityFeatures(self.memory.get_all(), data_collected).find_expenses_by_type()
            if len(expenses_found) == 0:
                expenses_found.append(f"There aren't any expenses in this category")
                return expenses_found
            else:
                return expenses_found
        else:
            return ["The apps does not contain that category"]

    def search_smaller_expenses(self, data_amount, data_date):
        expenses_amount = Expense("", data_amount, "")
        expenses_date = Expense(data_date, "", "")
        if expenses_amount.check_amount() and expenses_date.check_day_format():
            found_expenses = MultipleDataFeatures(self.memory.get_all(), data_date,
                                                  data_amount).display_lower_expenses()
            if len(found_expenses) == 0:
                found_expenses.append(f"There aren't any lower expenses till that day")
                return found_expenses
            else:
                return found_expenses
        else:
            return ["Wrong inputs, please try again!"]

    def display_sum_expenses(self, data_collected):
        expense = Expense("", "", data_collected)
        if expense.check_type():
            return [f"\nThe sum for {data_collected} category is: {EntityFeatures(self.memory.get_all(), data_collected).sum_expenses_by_type()}"]

    def display_maximum_spending(self):
        """The function takes the entire list of expenses and finds the most expensive day
              It returns a string/message, but it doesn't consider the month. Consider fixing it."""
        dates = SingleDataFeatures(self.memory.get_all()).get_date()
        days = SingleDataFeatures(self.memory.get_all()).get_multi_days()
        check_if_day_used = []
        list_with_amounts = []
        i = 0
        while len(self.memory.get_all()) > i:
            if days[i] == SingleDataFeatures(self.memory.get_all()).get_day(dates[i]) and days[i] not in check_if_day_used:
                list_with_amounts.append(SingleDataFeatures(self.memory.get_all()).sum_expenses_by_day(days[i]))
                check_if_day_used.append(days[i])
                i += 1
            else:
                i += 1
        the_result = 0
        dates_locations = SingleDataFeatures(self.memory.get_all()).find_date_location()
        for amount in list_with_amounts:
            if the_result < amount:
                the_result = amount

        print(
            f"\nThe most expensive day is {dates[dates_locations[list_with_amounts.index(the_result)]]}"
            f" with a total of {the_result} spent")

    def display_same_amount_expenses(self, data_collected):
        expense = Expense("", data_collected, "")
        if expense.check_amount():
            expense_found = EntityFeatures(self.memory.get_all(), data_collected).save_expenses_with_same_amount()
            if len(expense_found) == 0:
                return ["There aren't any expenses with same amount"]
            else:
                return expense_found
        else:
            return ["Please try to input an amount, nothing else"]

    def display_expenses_by_type(self, data_collected):
        expense = Expense("", "", data_collected)
        if expense.check_type():
            expense_found = EntityFeatures(self.memory.get_all(), data_collected).find_expenses_by_type()
            if len(expense_found) == 0:
                return [f"There aren't any expenses in this category"]
            else:
                expense_found.insert(0, f"\nThis is the list that is in {data_collected} category:")
                return expense_found
        else:
            return ["Please try to input a category/type"]

    def remove_smaller_expenses(self, data_collected):
        expense = Expense("", data_collected, "")
        if expense.check_amount():
            expenses_found = EntityFeatures(self.memory.get_all(), data_collected).save_higher_expenses()
            if len(expenses_found) == 0:
                print(f"There aren't any smaller expenses in the list")
            else:
                self.memory.remove_all()
                self.memory.add_to_repository(expenses_found)
