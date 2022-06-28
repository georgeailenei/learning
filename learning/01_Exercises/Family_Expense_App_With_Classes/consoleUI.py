from interface import UI
from entity import Expense
from console_memory import console_memory
import os


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

    def user_input(self):
        """The method returns the user input"""
        option = input("Choose and option: ")
        return option

    def main_menu(self):
        """The method prints the main menu"""
        print(self.menu)

    def submenu(self, option):
        """This method takes a variable as option to print the right submenu"""
        print(self.sub_menu[option])

    def exit_menu(self):
        """It returns False or True depending on the input"""
        option = input("\nDo you want to continue (Yes/No)? ")
        if option == "no" or option == "No":
            return False
        else:
            return True

    def display_all_expenses(self):
        """This function prints all expenses"""
        print("Current expenses list:")
        for expense in console_memory.get_all_expenses():
            print(expense)

    def display_expenses(self, expenses):
        """This function prints all expenses"""
        print("Expenses that you are looking for:")
        for expense in expenses:
            print(expense)

    def refresh(self):
        return os.system("cls")

    def refresh_display_expenses(self):
        return ConsoleUI().refresh(), ConsoleUI().display_all_expenses()

    @staticmethod
    def collected_data():
        """This method collects the data from the user and returns an object"""
        expense_date = input("\nDate (dd-mm-yy): ")
        expense_amount = input("Amount: ")
        expense_type = input("Type (Food, Bills, Clothes, Phone or Other): ")
        return Expense(expense_date, expense_amount, expense_type)
