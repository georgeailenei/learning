from console_memory import console_memory, Remove, repository
from entity_features import EntityFeatures, MultipleDataFeatures
from consoleUI import ConsoleUI
from entity import Expense


class Filters:
    def __init__(self, data_collected):
        self.data_collected = data_collected

    def check_data(self):
        """This functions checks the format of the data given"""
        if Expense.check_all_data(self.data_collected):
            console_memory.save(self.data_collected.__repr__())
            print(f"The expense - {self.data_collected} - has been added to the list\n")
        else:
            print("Please try to input your data again!")

    def check_all_data(self):
        """This functions checks the format only and returns the boolean True"""
        if Expense.check_all_data(self.data_collected):
            return True

    def check_to_update(self):
        """This function just if the input is in the repository
        It gets the index and replaces it with a new user input"""
        update_the_expense = self.data_collected.__repr__()

        if update_the_expense in repository:
            expense_location = repository.index(update_the_expense)
            repository.remove(update_the_expense)

            while True:
                print("\nUpdate your expense")
                new_expense = ConsoleUI.collected_data()
                update_the_expense = new_expense.__repr__()

                if Filters(new_expense).check_all_data():
                    repository.insert(expense_location, update_the_expense)
                    break
                else:
                    print("Please try to input your data again!")
        else:
            print("We could not find your expense, try again!\n")

    def check_date_to_remove(self):
        date = Expense(self.data_collected, "", "")

        if date.check_date_format():
            update_expenses = Remove(repository, self.data_collected).remove()
            console_memory.remove_all()
            console_memory.add_to_repository(update_expenses)
        else:
            print("Please write in this format (dd-mm-yy)")

    def check_type_to_remove(self):
        expense_type = Expense("", "", self.data_collected)

        if expense_type.check_type():
            update_expenses = Remove(repository, self.data_collected).remove()
            console_memory.remove_all()
            console_memory.add_to_repository(update_expenses)
        else:
            print("The app does not support that type of expense")

    def check_amount_to_find(self):
        expense = Expense("", self.data_collected, "")

        if expense.check_amount():
            found_expenses = EntityFeatures(repository, self.data_collected).find_greater_expenses()
            if len(found_expenses) == 0:
                print(f"There aren't bigger numbers than {self.data_collected}")
            else:
                ConsoleUI().display_expenses(found_expenses)
        else:
            print("\nPlease insert a number not random things.")

    def check_type_to_find(self):
        expense = Expense("", "", self.data_collected)

        if expense.check_type():
            expenses_found = EntityFeatures(repository, self.data_collected).find_expenses_by_type()
            if len(expenses_found) == 0:
                print(f"There aren't any expenses in this category")
            else:
                ConsoleUI().display_expenses(expenses_found)
        else:
            print("\nThe apps does not contain that category")

    def check_type_to_display(self):
        expense = Expense("", "", self.data_collected)

        if expense.check_type():
            print(f"\nThe sum for {self.data_collected} category is: {EntityFeatures(repository, self.data_collected).sum_expenses_by_type()}")
        else:
            print("The app does not contain that category")

    def find_expenses_with_same_amount(self):
        expense = Expense("", self.data_collected, "")

        if expense.check_amount():
            expense_found = EntityFeatures(repository, self.data_collected).save_expenses_with_same_amount()
            if len(expense_found) == 0:
                print(f"There aren't any expenses with same amount")
            else:
                print(f"\nThis is the list which contains the amount of {self.data_collected}:")
                ConsoleUI().display_expenses(expense_found)
        else:
            print("Please try to input an amount, nothing else")

    def display_expenses_by_type(self):
        expense = Expense("", "", self.data_collected)

        if expense.check_type():
            expense_found = EntityFeatures(repository, self.data_collected).find_expenses_by_type()
            if len(expense_found) == 0:
                print(f"There aren't any expenses in this category")
            else:
                print(f"\nThis is the list that is in {self.data_collected} category:")
                ConsoleUI().display_expenses(expense_found)
        else:
            print("Please try to input a category/type")

    def check_amount_to_remove(self):
        expense = Expense("", self.data_collected, "")

        if expense.check_amount():
            expenses_found = EntityFeatures(repository, self.data_collected).save_higher_expenses()
            if len(expenses_found) == 0:
                print(f"There aren't any smaller expenses in the list")
            else:
                console_memory.remove_all()
                console_memory.add_to_repository(expenses_found)


class FiltersMultipleData:
    def __init__(self, data_collected, data_collected_two):
        self.data_collected = data_collected
        self.data_collected_two = data_collected_two

    def check_amount_date_to_find(self):
        expenses_amount = Expense("", self.data_collected, "")
        expenses_date = Expense(self.data_collected_two, "", "")

        if expenses_amount.check_amount() and expenses_date.check_day_format():
            found_expenses = MultipleDataFeatures(repository, self.data_collected_two, self.data_collected).display_lower_expenses()
            if len(found_expenses) == 0:
                print(f"There aren't any lower expenses till that day")
            else:
                ConsoleUI().display_expenses(found_expenses)
        else:
            print("\nWrong inputs, please try again!")

    def check_day_format_to_remove(self):
        dates = [Expense(self.data_collected, "", ""), Expense(self.data_collected, "", "")]

        if dates[0].check_date_format() and dates[1].check_date_format():
            if dates[0].check_day_format() and dates[1].check_day_format():
                MultipleDataFeatures(repository, self.data_collected, self.data_collected_two).remove_by_time_interval()
        else:
            print("\nPlease try to input a date again.\n")
