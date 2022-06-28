import repository

class UI:
    """User interface menu and options"""
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
                          "3. Print smaller expenses than in put and before the given day \n"
                          "4. Return to main menu \n",
                "Reports": "1. Print sum of all expenses from a category \n"
                           "2. Find the max expense in a day \n"
                           "3. Print all expenses with the same amount \n"
                           "4. Print all expenses by category \n"
                           "5. Return to main menu \n",
                "Filters": "1. Remove all expenses by category \n"
                           "2. Remove smaller expenses \n"
                           "3. Return to main menu \n"}

    # Variables that collects data
    expense_date = input("\nDate (dd-mm-yy): ")
    expense_amount = input("Amount: ")
    expense_type = input("Type (Food, Bills, Clothes, Phone or Other): ")

    # Choose option variables
    choose = input("Choose an option: ")
    option = input("Do you want to continue: ")

    # Display expenses
    tittle = "  Date  ", "  Amount  ", "  Type"

    def main_menu(self):
        """Prints the main menu"""
        print(self.menu)


    def submenu(self, option):
        """This method takes a variable as option to print the right submenu"""
        print(self.sub_menu[option])


    def collect_data(self):
        """This method collects data"""
        expense_date = self.expense_date
        expense_amount = self.expense_amount
        expense_type = self.expense_type
        return repository.Expense(expense_date, expense_amount, expense_type)


    def choose_option(self):
        return self.choose


    def exit_to_menu(self):
        """It returns False or True depending on the input"""
        option = self.option
        if option == "no" or option == "No":
            return False
        else:
            return True


    def display_expenses(self, expenses):
        print(self.tittle)
        for i in expenses:
            print("   ".join(i))

