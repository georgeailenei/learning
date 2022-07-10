from entity_features import MultipleDataFeatures, EntityFeatures, SingleDataFeatures
from entity import Expense


class ControllerError(Exception):
    pass


class Controller:
    def __init__(self, repository, validator):
        self.repository = repository
        self.validator = validator

    def expense_list(self):
        return self.repository.get_all()

    def add_expense(self, expense):
        if self.validator.validate(expense):
            self.repository.save(expense)
            self.repository.timeline()
            print(self.repository.timeline())
        else:
            print("Please try to input your data again!")

    def check_expense_list(self):
        return len(self.repository.get_all()) != 0

    def update_expenses(self, id_of_expense_to_update, expense_date, expense_amount, expense_type):
        expense = self.repository.get(id_of_expense_to_update)
        if expense is None:
            raise ControllerError(f'Expense {id_of_expense_to_update} does not exist')

        expense.date = expense_date
        expense.amount = expense_amount
        expense.expense_type = expense_type
        if not self.validator.validate(expense):
            raise ControllerError(f'Expense {expense} is not valid')

        self.repository.update(expense)

    def remove_expenses_by_date(self, data_collected):
        date = Expense(data_collected, "", "")
        if date.check_date_format():
            update_expenses = self.repository.remove(data_collected)
            self.repository.remove_all()
            self.repository.save_all(update_expenses)
        else:
            print("Please write in this format (dd-mm-yy)")

    def remove_expenses_by_type(self, data_collected):
        expense_type = Expense("", "", data_collected)
        if expense_type.check_type():
            update_expenses = self.repository.remove(data_collected)
            self.repository.remove_all()
            self.repository.save_all(update_expenses)
        else:
            print("The app does not support that type of expense")

    def remove_by_time_interval(self, from_date, to_date):
        the_dates = SingleDataFeatures(self.repository.get_all()).get_date()
        the_month = [SingleDataFeatures(self.repository.get_all()).get_month(from_date), SingleDataFeatures(self.repository.get_all()).get_month(to_date)]
        remove_from_day = SingleDataFeatures(self.repository.get_all()).get_day(from_date)
        remove_to_day = SingleDataFeatures(self.repository.get_all()).get_day(to_date)
        update_expenses = []
        i = 0

        if the_month[0] == the_month[1]:
            while len(self.repository.get_all()) > i:
                if remove_from_day <= SingleDataFeatures(self.repository.get_all()).get_day(the_dates[i]) <= remove_to_day:
                    i += 1
                else:
                    update_expenses.append(self.repository.get_all()[i])
                    i += 1
            self.repository.remove_all()
            self.repository.save_all(update_expenses)
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
            found_expenses = EntityFeatures(self.repository.get_all(), data_collected).find_greater_expenses()
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
            expenses_found = EntityFeatures(self.repository.get_all(), data_collected).find_expenses_by_type()
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
            found_expenses = MultipleDataFeatures(self.repository.get_all(), data_date,
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
            return [f"\nThe sum for {data_collected} category is: {EntityFeatures(self.repository.get_all(), data_collected).sum_expenses_by_type()}"]

    def display_maximum_spending(self):
        """The function takes the entire list of expenses and finds the most expensive day
              It returns a string/message, but it doesn't consider the month. Consider fixing it."""
        dates = SingleDataFeatures(self.repository.get_all()).get_date()
        days = SingleDataFeatures(self.repository.get_all()).get_multi_days()
        check_if_day_used = []
        list_with_amounts = []
        i = 0
        while len(self.repository.get_all()) > i:
            if days[i] == SingleDataFeatures(self.repository.get_all()).get_day(dates[i]) and days[i] not in check_if_day_used:
                list_with_amounts.append(SingleDataFeatures(self.repository.get_all()).sum_expenses_by_day(days[i]))
                check_if_day_used.append(days[i])
                i += 1
            else:
                i += 1
        the_result = 0
        dates_locations = SingleDataFeatures(self.repository.get_all()).find_date_location()
        for amount in list_with_amounts:
            if the_result < amount:
                the_result = amount

        print(
            f"\nThe most expensive day is {dates[dates_locations[list_with_amounts.index(the_result)]]}"
            f" with a total of {the_result} spent")

    def display_same_amount_expenses(self, data_collected):
        expense = Expense("", data_collected, "")
        if expense.check_amount():
            expense_found = EntityFeatures(self.repository.get_all(), data_collected).save_expenses_with_same_amount()
            if len(expense_found) == 0:
                return ["There aren't any expenses with same amount"]
            else:
                return expense_found
        else:
            return ["Please try to input an amount, nothing else"]

    def display_expenses_by_type(self, data_collected):
        expense = Expense("", "", data_collected)
        if expense.check_type():
            expense_found = EntityFeatures(self.repository.get_all(), data_collected).find_expenses_by_type()
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
            expenses_found = EntityFeatures(self.repository.get_all(), data_collected).save_higher_expenses()
            if len(expenses_found) == 0:
                print(f"There aren't any smaller expenses in the list")
            else:
                self.repository.remove_all()
                self.repository.save_all(expenses_found)

    def undo(self, option):
        timeline = self.repository.timeline()
        tail = -1
        step = 0

        if option == "yes":
            if timeline[tail] == self.repository:
                step += 1
                previous_expenses = timeline[tail - step]
                self.repository.remove_all()
                self.repository.save_all(previous_expenses)
