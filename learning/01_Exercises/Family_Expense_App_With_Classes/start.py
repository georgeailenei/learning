from control import Controller
from consoleUI import ConsoleUI


class Start:
    def __init__(self, option):
        self.UI = ConsoleUI()
        self.option = option

    def chosen_option(self):
        # Add expenses
        if self.option == "1":
            Controller().adding_expenses()

        # Update expenses
        elif self.option == "2":
            Controller().update_expense()

        # Remove expenses
        elif self.option == "3":
            while True:
                self.UI.refresh()
                self.UI.submenu("Remove")
                option = self.UI.user_input()

                # Remove expenses by inserting dates
                if option == "1":
                    Controller().remove_expenses_by_date()

                # Remove expenses by type
                elif option == "2":
                    Controller().remove_expenses_by_type()

                # Remove expenses by time
                elif option == "3":
                    Controller().remove_expenses_by_time()

                # Return to main menu
                elif option == "4":
                    break

        # Print the full list with expenses
        elif self.option == "4":
            while True:
                self.UI.refresh_display_expenses()
                if not self.UI.exit_menu():
                    break

        # Search for expenses
        elif self.option == "5":
            while True:
                self.UI.refresh()
                self.UI.submenu("Search")
                option = self.UI.user_input()

                # Print all expenses higher than input
                if option == "1":
                    Controller().search_higher_expenses()

                # Print all expenses of the same type
                elif option == "2":
                    Controller().search_same_type_expeses()

                # Print smaller expenses than input and before the given day
                elif option == "3":
                    Controller().search_smaller_expenses()

                # Return to main menu
                elif option == "4":
                    break

        # Reports
        elif self.option == "6":
            while True:
                self.UI.refresh()
                self.UI.submenu("Reports")
                option = self.UI.user_input()

                # Display the sum of all expenses from a category
                if option == "1":
                    Controller().display_sum_expenses()

                # Find the max expense in a day
                elif option == "2":
                    Controller().display_maximum_spending()

                # Print all expenses with the same amount
                elif option == "3":
                    Controller().display_expenses_amount()

                # Print all expenses by category
                elif option == "4":
                    Controller().display_expenses_by_type()

                # Return to main menu
                elif option == "5":
                    break

        # Filters
        elif self.option == "7":
            while True:
                self.UI.refresh()
                self.UI.submenu("Filters")
                option = self.UI.user_input()

                # Remove all expenses by category
                if option == "1":
                    Controller().remove_expenses_by_type()

                # Remove smaller expenses
                elif option == "2":
                    Controller().remove_smaller_expenses()

                # Return to main menu
                elif option == "3":
                    break

        # Stop app
        elif self.option == "9":
            return "stop"
