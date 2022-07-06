from abc import ABC, abstractmethod
from entity import Expense
import os
from control import ControllerError


class UI(ABC):
    @abstractmethod
    def user_input(self):
        pass


class ConsoleUI(UI):
    """Console user interface menu and submenus"""
    menu = '1. Add expenses \n' \
           '2. Update expenses \n' \
           '3. Remove expenses \n' \
           '4. Print full list of expenses \n' \
           '5. Search for expenses \n' \
           '6. Reports \n' \
           '7. Filters \n' \
           '8. Undo \n' \
           '9. Exit \n'

    sub_menu = {"Remove": "1. Remove all expenses by date \n"
                          "2. Remove all expenses by type \n"
                          "3. Remove expenses by a time interval \n"
                          "4. Return to main menu \n",
                "Search": "1. Print all expenses higher than input \n"
                          "2. Print all expenses of the same type \n"
                          "3. Print smaller expenses than the input and before the given day \n"
                          "4. Return to main menu \n",
                "Reports": "1. Print sum of all expenses from a category \n"
                           "2. Find the max expense in a day \n"
                           "3. Print all expenses with the same amount \n"
                           "4. Print all expenses by category \n"
                           "5. Return to main menu \n",
                "Filters": "1. Remove all expenses by category \n"
                           "2. Remove smaller expenses \n"
                           "3. Return to main menu \n"}

    errors = {"addExpenses": "The list is empty please add expenses and than come back here to update if necessary",
              "emptyList": "The list is empty please add expenses to see the most expensive day"}

    data_type = {"Question": "\nDo you want to continue (Yes/No)? ",
                 "Choose": "Choose and option: ",
                 "Date": "\nDate (dd-mm-yy): ",
                 "Amount": "Write an amount: ",
                 "Type": "Type (Food, Bills, Clothes, Phone or Other): "}

    titles = {"expenseList": "\nCurrent expense list:",
              "addExpenses": "Add an expense",
              "updateExpense": "Select an expense to update",
              "update": "\nWrite the new expense",
              "removeDates": "Please insert a date",
              "removeType": "Please insert a category - Food, Bills, Clothes, Phone or Other",
              "removeByTime": "Please insert a time interval in date format to remove expenses",
              "removeSmallerExpenses": "Please write an amount",
              "findHigherExpenses": "Please write an amount",
              "findSameTypeExpenses": "Please write a category - Food, Bills, Clothes, Phone or Other",
              "findSmallerExpenses": "Please write an amount and a date",
              "sumExpensesByCategory": "Please write a category - Food, Bills, Clothes, Phone or Other",
              "displayExpensesWithSameAmount": "Please write an amount",
              "displayExpensesByCategory": "Please write a category - Food, Bills, Clothes, Phone or Other"}

    def __init__(self, controller):
        self.controller = controller

    def user_input(self):
        """The method returns the user input"""
        option = input(self.display_data_type("Choose"))
        return option

    def main_menu(self):
        print(self.menu)

    def submenu(self, option):
        print(self.sub_menu[option])

    def exit(self):
        """It returns False or True depending on the input"""
        option = input(self.display_data_type("Question"))
        if option == "no" or option == "No":
            return False
        elif option == "yes" or option == "Yes":
            return True
        else:
            return False

    def display_data_type(self, option):
        return self.data_type[option]

    def display_title(self, option):
        print(self.titles[option])

    def display_error(self, option):
        print(self.errors[option])

    def display_all_expenses(self):
        """This function prints all expenses"""
        self.display_title("expenseList")
        for expense in self.controller.expense_list():
            print(f'{expense.id}. {expense.date} {expense.amount} {expense.expense_type}')

    @staticmethod
    def display_found_expenses(expenses):
        for expense in expenses:
            print(expense)

    def refresh(self):
        return os.system("cls")

    def collected_data(self):
        """This method collects the data from the user and returns an object"""
        expense_date = input("\nDate (dd-mm-yy): ")
        expense_amount = input("Amount: ")
        expense_type = input("Type (Food, Bills, Clothes, Phone or Other): ")
        return Expense(expense_date, expense_amount, expense_type)

    def display_adding_expenses(self):
        while True:
            self.display_title("addExpenses")
            expense = self.collected_data()
            self.controller.add_expense(expense)
            self.display_all_expenses()
            if not self.exit():
                break

    def update_expenses(self):
        while True:
            self.display_all_expenses()
            self.display_title("updateExpense")

            id_ = int(input('\nId:'))
            expense_date = input("\nDate (dd-mm-yy): ")
            expense_amount = input("Amount: ")
            expense_type = input("Type (Food, Bills, Clothes, Phone or Other): ")

            try:
                self.controller.update_expenses(id_, expense_date, expense_amount, expense_type)
            except ControllerError as ex:
                print(str(ex))

            if not self.exit():
                break

    def remove_expenses_by_date(self):
        while True:
            self.refresh()
            self.display_title("removeDates")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Date"))
            self.controller.remove_expenses_by_date(data_collected)
            self.display_all_expenses()
            if not self.exit():
                break

    def remove_expenses_by_type(self):
        while True:
            self.refresh()
            self.display_title("removeType")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Type"))
            self.controller.remove_expenses_by_type(data_collected)
            self.display_all_expenses()
            if not self.exit():
                break

    def remove_expenses_by_time(self):
        while True:
            self.refresh()
            self.display_title("removeByTime")
            self.display_all_expenses()
            from_date = input(self.display_data_type("Date"))
            to_date = input(self.display_data_type("Date"))
            self.controller.remove_expenses_by_time(from_date, to_date)
            self.display_all_expenses()
            if not self.exit():
                break

    def search_higher_expenses(self):
        while True:
            self.refresh()
            self.display_title("findHigherExpenses")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Amount"))
            data_found = self.controller.search_higher_expenses(data_collected)
            self.display_found_expenses(data_found)
            if not self.exit():
                break

    def search_same_type_expenses(self):
        while True:
            self.refresh()
            self.display_title("findSameTypeExpenses")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Type"))
            data_found = self.controller.search_same_type_expenses(data_collected)
            self.display_found_expenses(data_found)
            if not self.exit():
                break

    def search_smaller_expenses(self):
        while True:
            self.refresh()
            self.display_title("findSmallerExpenses")
            self.display_all_expenses()
            data_amount = input(self.display_data_type("Amount"))
            data_date = input(self.display_data_type("Date"))
            data_found = self.controller.search_smaller_expenses(data_amount, data_date)
            self.display_found_expenses(data_found)
            if not self.exit():
                break

    def display_sum_expenses(self):
        while True:
            self.refresh()
            self.display_title("sumExpensesByCategory")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Type"))
            self.controller.display_sum_expenses(data_collected)
            if not self.exit():
                break

    def display_maximum_spending(self):
        while True:
            self.refresh()
            self.display_all_expenses()
            if self.controller.check_expense_list():
                self.controller.display_maximum_spending()
            else:
                self.display_error("emptyList")
            if not self.exit():
                break

    def display_same_amount_expenses(self):
        while True:
            self.refresh()
            self.display_title("displayExpensesWithSameAmount")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Amount"))
            data_found = self.controller.display_same_amount_expenses(data_collected)
            self.display_found_expenses(data_found)
            if not self.exit():
                break

    def display_expenses_by_type(self):
        while True:
            self.refresh()
            self.display_title("displayExpensesByCategory")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Type"))
            data_found = self.controller.display_expenses_by_type(data_collected)
            self.display_found_expenses(data_found)
            if not self.exit():
                break

    def remove_expenses_type(self):
        while True:
            self.refresh()
            self.display_title("removeType")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Type"))
            self.controller.remove_expenses_by_type(data_collected)
            self.display_all_expenses()
            if not self.exit():
                break

    def remove_smaller_expenses(self):
        while True:
            self.refresh()
            self.display_title("removeSmallerExpenses")
            self.display_all_expenses()
            data_collected = input(self.display_data_type("Amount"))
            self.controller.remove_smaller_expenses(data_collected)
            self.display_all_expenses()
            if not self.exit():
                break

    def start(self):
        while True:
            self.refresh()
            self.main_menu()
            option = self.user_input()
            self.refresh()

            # Add expenses
            if option == "1":
                self.display_adding_expenses()

            # Update expenses
            elif option == "2":
                self.update_expenses()

            # Remove expenses
            elif option == "3":
                while True:
                    self.submenu("Remove")
                    option = self.user_input()

                    # Remove expenses by inserting dates
                    if option == "1":
                        self.remove_expenses_by_date()

                    # Remove expenses by type
                    elif option == "2":
                        self.remove_expenses_by_type()

                    # Remove expenses by time
                    elif option == "3":
                        self.remove_expenses_by_time()

                    # Return to main menu
                    elif option == "4":
                        break

            # Print the full list with expenses
            elif option == "4":
                while True:
                    self.display_all_expenses()
                    if not self.exit():
                        break

            # Search for expenses
            elif option == "5":
                while True:
                    self.submenu("Search")
                    option = self.user_input()

                    # Print all expenses higher than input
                    if option == "1":
                        self.search_higher_expenses()

                    # Print all expenses of the same type
                    elif option == "2":
                        self.search_same_type_expenses()

                    # Print smaller expenses than input and before the given day
                    elif option == "3":
                        self.search_smaller_expenses()

                    # Return to main menu
                    elif option == "4":
                        break

            # Reports
            elif option == "6":
                while True:
                    self.submenu("Reports")
                    option = self.user_input()

                    # Display the sum of all expenses from a category
                    if option == "1":
                        self.display_sum_expenses()

                    # Find the max expense in a day
                    elif option == "2":
                        self.display_maximum_spending()

                    # Print all expenses with the same amount
                    elif option == "3":
                        self.display_same_amount_expenses()

                    # Print all expenses by category
                    elif option == "4":
                        self.display_expenses_by_type()

                    # Return to main menu
                    elif option == "5":
                        break

            # Filters
            elif option == "7":
                while True:
                    self.submenu("Filters")
                    option = self.user_input()

                    # Remove all expenses by category
                    if option == "1":
                        self.remove_expenses_type()

                    # Remove smaller expenses
                    elif option == "2":
                        self.remove_smaller_expenses()

                    # Return to main menu
                    elif option == "3":
                        break

            # Stop app
            elif option == "9":
                break
