from abc import ABC, abstractmethod
from entity import Expense
import os


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

    options = {"Write": "Please write your expense",
               "Error": "Please write yes or no",
               "Update Expense": "Select the expense for update\n",
               "Update": "\nWrite the new expense",
               "Question": "\nDo you want to continue (Yes/No)? ",
               "Choose": "Choose and option: "}

    data_type = {"Date": "\nDate (dd-mm-yy): ",
                 "Amount": "Write an amount: ",
                 "Type": "Type (Food, Bills, Clothes, Phone or Other): ",
                 "From date": "\nDate (dd-mm-yy): ",
                 "To date": "Date (dd-mm-yy): "}

    def __init__(self, controller):
        self.controller = controller

    def user_input(self):
        """The method returns the user input"""
        option = input(self.display_options_text("Choose"))
        return option

    def main_menu(self):
        print(self.menu)

    def submenu(self, option):
        print(self.sub_menu[option])

    def exit(self):
        """It returns False or True depending on the input"""
        option = input(self.display_options_text("Question"))
        if option == "no" or option == "No":
            return False
        elif option == "yes" or option == "Yes":
            return True
        else:
            return False

    def display_options_text(self, option):
        print(self.options[option])

    def get_data_type(self, option):
        print(self.data_type[option])

    def display_all_expenses(self):
        """This function prints all expenses"""
        print("\nCurrent expenses list:")
        for expense in self.controller.expense_list():
            print(expense)

    @staticmethod
    def refresh():
        return os.system("cls")

    @staticmethod
    def collected_data():
        """This method collects the data from the user and returns an object"""
        expense_date = input("\nDate (dd-mm-yy): ")
        expense_amount = input("Amount: ")
        expense_type = input("Type (Food, Bills, Clothes, Phone or Other): ")
        return Expense(expense_date, expense_amount, expense_type)

    def display_adding_expenses(self):
        self.refresh()
        self.display_options_text("Write")
        data_collected = self.collected_data()
        self.controller.adding_expenses(data_collected)
        self.display_all_expenses()

    def update_expenses(self):
        self.refresh()
        self.display_options_text("Update Expense")
        self.display_all_expenses()
        data_collected = self.collected_data()
        self.display_options_text("Update")
        updated_expense = self.collected_data()
        self.controller.update_expenses(data_collected, updated_expense)
        self.display_all_expenses()

    def remove_expenses_by_date(self):
        self.refresh()
        self.display_all_expenses()
        data_collected = input(self.get_data_type("Date"))
        self.controller.remove_expenses_by_date(data_collected)
        self.display_all_expenses()

    def remove_expenses_by_type(self):
        self.refresh()
        self.display_all_expenses()
        data_collected = input(self.get_data_type("Type"))
        self.controller.remove_expenses_by_type(data_collected)
        self.display_all_expenses()

    def remove_expenses_by_time(self):
        self.refresh()
        self.display_all_expenses()
        from_date = input(self.get_data_type("From Date"))
        to_date = input(self.get_data_type("To Date"))
        self.controller.remove_expenses_by_time(from_date, to_date)
        self.display_all_expenses()

    def display_maximum_spending(self):
        self.controller.display_sum_expenses()
        self.refresh()
        self.display_all_expenses()

    def start(self):
        while True:
            self.refresh()
            self.main_menu()
            option = self.user_input()

            # Add expenses
            if option == "1":
                while True:
                    self.display_adding_expenses()
                    if not self.exit():
                        break

            # Update expenses
            elif option == "2":
                while True:
                    self.update_expenses()
                    if not self.exit():
                        break

            # Remove expenses
            elif option == "3":
                while True:
                    self.refresh()
                    self.submenu("Remove")
                    option = self.user_input()

                    # Remove expenses by inserting dates
                    if option == "1":
                        while True:
                            self.remove_expenses_by_date()
                            if not self.exit():
                                break

                    # Remove expenses by type
                    elif option == "2":
                        while True:
                            self.remove_expenses_by_type()
                            if not self.exit():
                                break

                    # Remove expenses by time
                    elif option == "3":
                        while True:
                            self.remove_expenses_by_time()
                            if not self.exit():
                                break

                    # Return to main menu
                    elif option == "4":
                        break

            # # Print the full list with expenses
            # elif option == "4":
            #     while True:
            #         self.refresh()
            #         self.display_all_expenses()
            #         if not self.exit_menu():
            #             break
            #
            # # Search for expenses
            # elif option == "5":
            #     while True:
            #         self.refresh()
            #         self.submenu("Search")
            #         option = self.user_input()
            #
            #         # Print all expenses higher than input
            #         if option == "1":
            #             self.controller.search_higher_expenses()
            #
            #         # Print all expenses of the same type
            #         elif option == "2":
            #             self.controller.search_same_type_expeses()
            #
            #         # Print smaller expenses than input and before the given day
            #         elif option == "3":
            #             self.controller.search_smaller_expenses()
            #
            #         # Return to main menu
            #         elif option == "4":
            #             break
            #
            # # Reports
            # elif option == "6":
            #     while True:
            #         self.refresh()
            #         self.submenu("Reports")
            #         option = self.user_input()
            #
            #         # Display the sum of all expenses from a category
            #         if option == "1":
            #             self.controller.display_sum_expenses()
            #
            #         # Find the max expense in a day
            #         elif option == "2":
            #             self.display_maximum_spending()
            #
            #         # Print all expenses with the same amount
            #         elif option == "3":
            #             self.controller.display_expenses_amount()
            #
            #         # Print all expenses by category
            #         elif option == "4":
            #             self.controller.display_expenses_by_type()
            #
            #         # Return to main menu
            #         elif option == "5":
            #             break
            #
            # # Filters
            # elif option == "7":
            #     while True:
            #         self.refresh()
            #         self.submenu("Filters")
            #         option = self.user_input()
            #
            #         # Remove all expenses by category
            #         if option == "1":
            #             self.controller.remove_expenses_by_type()
            #
            #         # Remove smaller expenses
            #         elif option == "2":
            #             self.controller.remove_smaller_expenses()
            #
            #         # Return to main menu
            #         elif option == "3":
            #             break

            # Stop app
            elif option == "9":
                break
