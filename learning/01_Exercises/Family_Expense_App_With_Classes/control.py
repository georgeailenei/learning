from filters import Filters, FiltersMultipleData
from consoleUI import ConsoleUI
from console_memory import repository
from entity_features import SingleDataFeatures

UI = ConsoleUI()


class Controller:
    def __init__(self, repository):
        self.repository = repository

    def adding_expenses(self):
        while True:
            # Interface
            UI.refresh()
            print("Please write your expense")

            # Collecting data & filters
            data_collected = ConsoleUI.collected_data()
            Filters(data_collected).check_data()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break

    def update_expense(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Collecting data & filters
            data_collected = ConsoleUI.collected_data()
            Filters(data_collected).check_to_update()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break

    def remove_expenses_by_date(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Collecting data & filters
            data_collected = input("Date (dd-mm-yy): ")
            Filters(data_collected).check_date_to_remove()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break

    def remove_expenses_by_type(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Collecting data & filters
            data_collected = input("Type (Food, Bills, Clothes, Phone or Other): ")
            Filters(data_collected).check_type_to_remove()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break

    def remove_expenses_by_time(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Collecting data & filters
            from_date = input("From Date (dd-mm-yy): ")
            to_date = input("To Date (dd-mm-yy): ")
            FiltersMultipleData(from_date, to_date).check_day_format_to_remove()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break

    def search_higher_expenses(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Collecting data & filters
            data_collected = input("\nWrite amount: ")
            Filters(data_collected).check_amount_to_find()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break

    def search_same_type_expeses(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Collecting data & filters
            data_collected = input("\nWrite type (Food, Bills, Clothes, Phone or Other): ")
            Filters(data_collected).check_type_to_find()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break

    def search_smaller_expenses(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Collecting data & filters
            data_collected = input("\nWrite amount: ")
            data_collected_two = input("Write day: ")
            FiltersMultipleData(data_collected, data_collected_two).check_amount_date_to_find()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break

    def display_sum_expenses(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Collecting data & filters
            data_collected = input("\nWrite type (Food, Bills, Clothes, Phone or Other): ")
            Filters(data_collected).check_type_to_display()
            if not UI.exit_menu():
                break

    def display_maximum_spending(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Filters & return to main menu
            print(SingleDataFeatures(repository).expensive_day())
            if not UI.exit_menu():
                break

    def display_expenses_amount(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Filters & return to main menu
            data_collected = input("\nWrite amount: ")
            Filters(data_collected).find_expenses_with_same_amount()
            if not UI.exit_menu():
                break

    def display_expenses_by_type(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Filters & return to main menu
            data_collected = input("\nWrite type (Food, Bills, Clothes, Phone or Other): ")
            Filters(data_collected).display_expenses_by_type()
            if not UI.exit_menu():
                break

    def remove_smaller_expenses(self):
        while True:
            # Interface
            UI.refresh_display_expenses()

            # Filters & return to main menu
            data_collected = input("\nWrite amount: ")
            Filters(data_collected).check_amount_to_remove()

            # Display current list
            UI.display_all_expenses()
            if not UI.exit_menu():
                break
