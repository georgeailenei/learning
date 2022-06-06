import removeExpenses
import findExpenses
import reports
import repository
import interface
import os


#   Functions which interacts with the UI.
def choose_option():
    """The func returns """
    return input("Choose an option: ")


def exit_to_menu():
    """It returns False or True depending on the input"""
    option = input("Do you want to continue? ")
    if option == "no" or option == "No":
        return False
    else:
        return True


#   Functions.
def collect_data():
    """It collects the data and stores it as object"""
    the_date_of_expense = input("Date (dd-mm-yy): ")
    the_amount_of_expense = input("Amount: ")
    the_type_of_expense = input("Type (Food, Bills, Clothes, Phone or Other): ")
    return repository.Expense(the_date_of_expense, the_amount_of_expense, the_type_of_expense)


def find_data_location(all_expenses, data):
    location = []

    for i in range(len(all_expenses)):
        if data == all_expenses[i]:
            location.append(i)

    return location


def check_expense_by_day(the_date):
    the_day = []

    for day in the_date:
        if day == "-":
            break
        else:
            the_day.append(day)

    for i in the_day:
        if i == "0":
            the_day.remove(i)

    the_actual_day = "".join(the_day)
    return int(the_actual_day)


# insert the code here
def get_date(all_expenses):
    """This function returns the date from expenses"""
    list_with_dates = []
    i = 0

    for date in all_expenses:
        list_with_dates.append(date[i])

    return list_with_dates


def get_day(all_expenses):
    """This function returns the day from the date"""
    """Also it using get_date func."""
    list_with_dates = get_date(all_expenses)
    list_with_days = []
    j = 0
    i = 0

    for day in list_with_dates:
        for num in day:
            if num == "-":
                list_with_days.append(day[i:j])
                j = 0
                break
            else:
                j += 1

    return list_with_days


def get_expenses_by_amount(all_expenses):
    list_with_all_amounts = []
    the_expenses_list = []
    i = 1

    for amount in all_expenses:
        list_with_all_amounts.append(amount[i])

    # get input from the user
    the_amount = input("Please insert the expense amount: ")

    for amount in all_expenses:
        if the_amount in amount[i]:
            the_expenses_list.append(amount)

    return the_expenses_list


def get_expenses_by_category(all_expenses):
    list_with_all_categories = []
    the_expenses_list = []
    i = 2

    for amount in all_expenses:
        list_with_all_categories.append(amount[i])

    # get input from the user
    the_category = input("Please insert the category: ")

    for category in all_expenses:
        if the_category in category[i]:
            the_expenses_list.append(category)

    return the_expenses_list


def remove_expenses_by_category(all_expenses):
    # get input from the user
    the_category = input("Please insert the category: ")
    new_expenses_list = []
    i = 2

    for category in all_expenses:
        if the_category == category[i]:
            pass
        else:
            new_expenses_list.append(category)

    all_expenses = new_expenses_list

    return all_expenses


def remove_expense_by_amount(all_expenses):
    list_with_all_amounts = []
    expenses_tb_removed = []
    new_list_with_expenses = []
    i = 1

    for amount in all_expenses:
        list_with_all_amounts.append(amount[i])

    # get input from the user
    the_amount = input("Please insert the expense amount: ")

    for amount in all_expenses:
        if int(the_amount) > int(amount[i]):
            expenses_tb_removed.append(amount)

    for expense in all_expenses:
        if expense in expenses_tb_removed:
            pass
        else:
            new_list_with_expenses.append(expense)

    return new_list_with_expenses


# The main func which puts everything together.
def main():
    all_expenses = []

    while True:
        os.system("cls")
        user_interface = interface.UI()
        user_interface.main_menu()
        options = choose_option()

        if options == "1":  # add expenses
            while True:
                os.system("cls")
                print("\nPlease write your expenses")
                data_collected = collect_data()

                if repository.check_all_data(data_collected):
                    all_expenses.append(data_collected.get_all_expense_details())
                else:
                    print("Please try to input your data again!")

                os.system("cls")
                interface.display_expense(all_expenses)

                if not exit_to_menu():
                    break

        elif options == "2":  # update expenses
            while True:
                os.system("cls")
                print("Please choose the expense that you want to update")
                interface.display_expense(all_expenses)
                update_the_expense = collect_data()

                if update_the_expense.get_all_expense_details() in all_expenses:
                    expense_location = find_data_location(all_expenses, update_the_expense.get_all_expense_details())
                    all_expenses.remove(update_the_expense.get_all_expense_details())

                    while True:
                        print("\nUpdate your expense")
                        update_the_expense = collect_data()

                        if repository.check_all_data(update_the_expense):
                            all_expenses.insert(expense_location[0], update_the_expense.get_all_expense_details())
                            break
                        else:
                            print("Please try to input your data again!")

                else:
                    print("We could not find your expense, try again!")

                print("\nUpdated list")
                interface.display_expense(all_expenses)

                if not exit_to_menu():
                    break

        elif options == "3":    # Remove submenu
            while True:
                user_interface.submenu("Remove")
                options = choose_option()

                if options == "1":
                    while True:
                        print("\nYou can now remove and expense by inserting the Date")
                        interface.display_expense(all_expenses)

                        date_of_expense = input("Date (dd-mm-yy): ")
                        check_date = repository.Expense(date_of_expense, "", "")

                        if check_date.check_date_format():
                            all_expenses = removeExpenses.remove_expense(all_expenses, date_of_expense)
                            print("\nUpdated list")
                            interface.display_expense(all_expenses)
                        else:
                            print("Please try to use the date format (dd-mm-yy)")

                        if not exit_to_menu():
                            break

                elif options == "2":
                    while True:
                        print("\nYou can now remove expense by inserting the type/category")
                        interface.display_expense(all_expenses)

                        expense_type = input("Type (Food, Bills, Clothes, Phone or Other): ")
                        check_type = repository.Expense("", "", expense_type)

                        if check_type.check_type():
                            all_expenses = removeExpenses.remove_expense(all_expenses, expense_type)
                            print("\nUpdated list")
                            interface.display_expense(all_expenses)
                        else:
                            print("The app does not contain that type of expenses")

                        if not exit_to_menu():
                            break

                elif options == "3":
                    while True:
                        print("\nYou can now remove expense by time interval")
                        interface.display_expense(all_expenses)

                        from_day = input("From Date (dd-mm-yy): ")
                        to_day = input("To Date (dd-mm-yy): ")
                        dates = [repository.Expense(from_day, "", ""), repository.Expense(to_day, "", "")]

                        if dates[0].check_date_format() and dates[1].check_date_format():
                            if dates[0].check_day_format() and dates[1].check_day_format():
                                all_expenses = removeExpenses.remove_by_time_interval(all_expenses, from_day, to_day)
                                print("\nUpdated list")
                                interface.display_expense(all_expenses)
                        else:
                            print("\nPlease try to input a date again.\n")

                        if not exit_to_menu():
                            break

                elif options == "4":
                    break

        elif options == "4":
            print("\nThis is your list of expenses:")
            interface.display_expense(all_expenses)

            if not exit_to_menu():
                continue

        elif options == "5":
            while True:
                print("\nYou can now search for expenses")
                user_interface.submenu("Search")
                options = choose_option()

                if options == "1":
                    while True:
                        print("\nDisplay higher expenses\n")
                        interface.display_expense(all_expenses)

                        amount = input("\nWrite amount: ")
                        check_amount = repository.Expense("", amount, "")

                        if check_amount.check_amount():
                            interface.display_expense(findExpenses.find_greater_expenses(all_expenses, amount))
                        else:
                            print("\nPlease insert a number not random things.")

                        if not exit_to_menu():
                            break

                elif options == "2":
                    while True:
                        print("\nPrint expenses by type\n")
                        interface.display_expense(all_expenses)

                        expense_type = input("\nWrite type (Food, Bills, Clothes, Phone or Other): ")
                        check_type = repository.Expense("", "", expense_type)

                        if check_type.check_type():
                            interface.display_expense(findExpenses.find_expenses_by_type(all_expenses, expense_type))
                        else:
                            print("\nThe apps does not contain that category")

                        if not exit_to_menu():
                            break

                elif options == "3":
                    while True:
                        print("\nChoose a day and amount to print a list with smaller amounts from previous days\n")
                        interface.display_expense(all_expenses)

                        amount = input("\nWrite amount: ")
                        expense_date_day = input("Write day (dd): ")

                        check_amount = repository.Expense("", amount, "")
                        check_date = repository.Expense(expense_date_day, "", "")

                        if check_date.check_day_format() and check_amount.check_amount():
                            interface.display_expense(findExpenses.display_lower_expenses(all_expenses, expense_date_day, amount))
                        else:
                            print("\nWrong inputs, please try again!")

                        if not exit_to_menu():
                            break

                elif options == "4":
                    break

        elif options == "6":
            while True:
                print("\nReports\n")
                user_interface.submenu("Reports")
                options = choose_option()

                if options == "1":
                    while True:
                        print("Sum Up all the expenses in a category")
                        interface.display_expense(all_expenses)

                        expense_type = input("Write either (Food, Bills, Clothes, Phone or Other): ")
                        check_expense_type = repository.Expense("", "", expense_type)

                        if check_expense_type.check_type():
                            print("\n", f"The sum for {expense_type} category is: ", reports.sum_expenses_by_type(all_expenses, expense_type), "\n")
                        else:
                            print("The app does not contain that category")

                        if not exit_to_menu():
                            break

                elif options == "2":
                    while True:
                        print("This is the most expensive day -_-")
                        interface.display_expense(all_expenses)

                        if not exit_to_menu():
                            break

                elif options == "3":
                    print("Print all the expenses with the same amount")
                    print(get_expenses_by_amount(all_expenses))

                    if not exit_to_menu():
                        break

                elif options == "4":
                    print("Print all the expenses by category")
                    print(get_expenses_by_category(all_expenses))
                    if not exit_to_menu():
                        break

        elif options == "7":
            print("\nFilters - Various Actions")
            user_interface.submenu("Filters")
            options = choose_option()

            while True:
                if options == "1":
                    print("You can now remove all the expenses by category")
                    print(remove_expenses_by_category(all_expenses))

                    if not exit_to_menu():
                        break

                elif options == "2":
                    print("You can now remove all the smaller expenses")
                    print(remove_expense_by_amount(all_expenses))

                    if not exit_to_menu():
                        break

        elif options == "8":
            print("\nUndo")
            print("Are you sure that you want to go back in time? ")

            if not exit_to_menu():
                continue

        elif options == "9":  # exit app
            if len(all_expenses) == 0:
                print("You really didn't spend any money? ok. goodbye!")
                break
            else:
                break


if __name__ == '__main__':
    main()
