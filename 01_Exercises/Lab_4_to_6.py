"""
2. Ștergere.
• Șterge cheltuielile pentru un interval de timp (se dă ziua de început și
sfârșit, se șterg toate cheltuielile pentru perioada dată)
• Șterge toate cheltuielile de un anumit tip"""



class Expense:
    def __init__(self, date, amount, expense_type):  # the data that we're getting.
        self.date = date
        self.amount = amount
        self.expense_type = expense_type

    def check_date(self):
        list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
        check_date = list(self.date)

        if check_date[2] == "-" and check_date[5] == "-":
            for i in check_date:
                if i not in list_of_numbers:
                    return False
                else:
                    return True
        else:
            return False

    def check_amount(self):
        list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        check_amount = list(self.amount)

        for i in check_amount:
            if i not in list_of_numbers:
                return False
            else:
                return True

    def check_type(self):
        expense_type_list = ["Food", "Bills", "Clothes", "Phone", "Other"]

        if self.expense_type in expense_type_list:
            return True
        else:
            return False

    def get_all_expense_details(self):  # print all the details date, amount and type.
        return (self.date + " " + str(self.amount) + " " + self.expense_type).split()


def main_menu():    # information and options about the app.
    print("This App allows you to store your expenses.")
    the_option = input("1. Add expenses \n"
                       "2. Update expenses \n"
                       "3. Remove expenses \n"
                       "4. Print full list of expenses \n"
                       "5. Exit \n"
                       "Please choose an option here: ")
    return the_option


def remove_menu():    # the Menu for remove option.
    print("Choose from the options below")
    the_option = input("1. Remove all expenses by date \n"
                       "2. Remove all expenses by type \n"
                       "3. Remove expenses by time \n"
                       "4. Return to main menu \n"
                       "Please choose an option here: ")
    return the_option


def exit_to_menu():
    choose_option = input("Do you want to continue? ")
    if choose_option == "no":
        return False
    else:
        return True


def collect_data():     # collects the data and stores in as object.
    the_date_of_expense = input("Date (dd-mm-yy): ")
    the_amount_of_expense = input("Amount: ")
    the_type_of_expense = input("Type (Food, Bills, Clothes, Phone or Other): ")
    return Expense(the_date_of_expense, the_amount_of_expense, the_type_of_expense)


def update_expense():   # collects another set of data for update.
    update_input = collect_data()
    the_update = update_input.get_all_expense_details()
    return the_update


def main():     # the main func that puts everything together.
    all_expenses = []

    while True:
        options = main_menu()

        if options == "1":      # add expenses
            print("\nYou can now input your expenses")

            while True:
                data_collected = collect_data()
                if data_collected.check_date() and data_collected.check_amount() and data_collected.check_type():
                    all_expenses.append(data_collected.get_all_expense_details())
                else:
                    print("Please try to input your data again!")

                print(all_expenses)     # display the current list of expenses.
                if not exit_to_menu():
                    break

        elif options == "2":       # update expenses
            update_the_expense = update_expense()

            if update_the_expense in all_expenses:
                all_expenses.remove(update_the_expense)
                print("Insert a new expense to update")
                update_the_expense = update_expense()
                all_expenses.append(update_the_expense)
            else:
                print("We could not find your expense, try again!")

            if not exit_to_menu():
                continue

        elif options == "3":
            other_options = remove_menu()
            while True:
                if other_options == "1":
                    print("\nYou can now remove and expense by inserting the Date")
                    the_date_of_expense = input("Date (dd-mm-yy): ")

                    for expense in all_expenses:
                        if the_date_of_expense not in expense:
                            print(all_expenses)
                            f"The {expense} has been removed!"
                            all_expenses.remove(expense)
                            print("Your new expenses list is:")
                            print(all_expenses)

                    if not exit_to_menu():
                        continue

                elif other_options == "2":
                    pass

                elif other_options == "3":
                    pass

                elif other_options == "4":
                    break

        elif options == "4":
            print("\nThis is your list of expenses:")
            print(all_expenses)

            if not exit_to_menu():
                continue

        elif options == "5":       # exit app
            if len(all_expenses) == 0:
                print("You really didn't spend any money? ok. goodbye!")
                break
            else:
                break


if __name__ == '__main__':
    main()
