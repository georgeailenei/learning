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


def remove_expense_by_time_interval(expense_list, the_start_day, the_last_day):
    to_be_removed_list = []
    i = 0
    j = 0

    while len(expense_list) > i:
        if the_start_day in expense_list[i][j]:
            to_be_removed_list.append(expense_list[i])
            i += 1
        elif the_last_day in expense_list[i][j]:
            to_be_removed_list.append(expense_list[i])
            i += 1
        else:
            i += 1

    return to_be_removed_list


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


def sum_expenses(amount):
    the_sum = 0

    for i in amount:
        the_sum = the_sum + int(i)

    return the_sum


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


def sum_expenses_by_day(all_the_expenses):
    """This func returns the sum of all expenses for a given day"""
    expenses = all_the_expenses
    day = input("Write a day to sum up the expenses: ")
    sum_up_these_expenses = []
    the_sum = 0
    i = 0
    j = 0
    x = 1

    # make a list with the expenses that are related to the day.
    for it in expenses:
        if day in expenses[i][j]:
            sum_up_these_expenses.append(expenses[i][x])
            i += 1
        else:
            i += 1

    # sum the expenses. you might want to remove these two lines of code when implementing in the main file.
    for i in sum_up_these_expenses:
        the_sum = the_sum + int(i)

    return the_sum


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


def display_expense(expenses):
    print("  Date", "    Amount", "Type  ")
    for i in expenses:
        print("   ".join(i))


def check_all_data(data_collected):
    if data_collected.check_date_format() and data_collected.check_amount() and data_collected.check_type():
        if data_collected.check_day_format() and data_collected.check_month_format() and data_collected.check_year_format() and data_collected.check_amount_int():
            return True


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

                if check_all_data(data_collected):
                    all_expenses.append(data_collected.get_all_expense_details())
                else:
                    print("Please try to input your data again!")

                os.system("cls")
                display_expense(all_expenses)

                if not exit_to_menu():
                    break

        elif options == "2":  # update expenses
            while True:
                os.system("cls")
                print("Please choose the expense that you want to update")
                display_expense(all_expenses)
                update_the_expense = collect_data()

                if update_the_expense.get_all_expense_details() in all_expenses:
                    expense_location = find_data_location(all_expenses, update_the_expense.get_all_expense_details())
                    all_expenses.remove(update_the_expense.get_all_expense_details())

                    while True:
                        print("\nUpdate your expense")
                        update_the_expense = collect_data()

                        if check_all_data(update_the_expense):
                            all_expenses.insert(expense_location[0], update_the_expense.get_all_expense_details())
                            break
                        else:
                            print("Please try to input your data again!")

                else:
                    print("We could not find your expense, try again!")

                print("Updated list")
                display_expense(all_expenses)

                if not exit_to_menu():
                    break

        elif options == "3":
            user_interface.submenu("Remove")
            options = choose_option()

            while True:
                if options == "1":
                    print("\nYou can now remove and expense by inserting the Date")
                    the_date_of_expense = input("Date (dd-mm-yy): ")

                    print(all_expenses)

                    for expense in all_expenses:
                        if the_date_of_expense in expense:
                            all_expenses.remove(expense)

                    print("Your new expenses list is:")
                    print(all_expenses)

                    if not exit_to_menu():
                        break

                elif options == "2":
                    print("\nYou can now remove expense by inserting the type/category")
                    type_of_expense = input("Type (Food, Bills, Clothes, Phone or Other): ")

                    print(all_expenses)

                    for expense in all_expenses:
                        if type_of_expense in expense:
                            all_expenses.remove(expense)

                    print("Your new expenses list is:")
                    print(all_expenses)

                    if not exit_to_menu():
                        break

                elif options == "3":
                    print("\nYou can now remove expense by time interval")
                    the_start_date = input("Start Day Date (dd): ")
                    the_last_date = input("Last Day Date (dd): ")

                    to_be_remove_expenses = remove_expense_by_time_interval(all_expenses, the_start_date, the_last_date)

                    print("This is the list that its about to be remove")
                    print(to_be_remove_expenses)

                    for expense in to_be_remove_expenses:
                        if expense in all_expenses:
                            all_expenses.remove(expense)

                    print("Your new expenses list is:")
                    print(all_expenses)

                    if not exit_to_menu():
                        break

                elif options == "4":
                    break

        elif options == "4":
            print("\nThis is your list of expenses:")
            print(all_expenses)

            if not exit_to_menu():
                continue

        elif options == "5":
            print("\nYou can now search of an expense")
            user_interface.submenu("Search")
            options = choose_option()

            while True:
                if options == "1":
                    print("Write an expense and the APP will print all higher expenses")
                    the_expense = input("Write expense: ")
                    high_expenses_list = []
                    i = 0
                    j = 1

                    while len(all_expenses) > i:
                        if int(all_expenses[i][j]) > int(the_expense):
                            high_expenses_list.append(all_expenses[i][j])
                            i += 1
                        else:
                            i += 1

                    print(high_expenses_list)
                    if not exit_to_menu():
                        break

                elif options == "2":
                    print("You can now choose to print expenses by type")
                    expense_type = input("Write either (Food, Bills, Clothes, Phone or Other): ")
                    expenses_by_list = []
                    i = 0
                    j = 2

                    while len(all_expenses) > i:
                        if all_expenses[i][j] == expense_type:
                            expenses_by_list.append(all_expenses[i])
                            i += 1
                        else:
                            i += 1

                    print(expenses_by_list)
                    if not exit_to_menu():
                        break

                elif options == "3":
                    print("Choose a day and the amount to print the list")
                    expense_by_sum = input("Write expense: ")
                    expense_by_day = input("Write day: ")
                    expense_list = []
                    i = 0
                    j = 0
                    x = 1

                    while len(all_expenses) > i:
                        if check_expense_by_day(all_expenses[i][j]) < int(expense_by_day):
                            if int(expense_by_sum) > int(all_expenses[i][x]):
                                expense_list.append(all_expenses[i])
                                i += 1
                            else:
                                i += 1
                        else:
                            i += 1

                    print(expense_list)
                    if not exit_to_menu():
                        break

                elif options == "4":
                    break

        elif options == "6":
            print("\nReports - various actions for the expense list")
            user_interface.submenu("Reports")
            options = choose_option()

            while True:
                if options == "1":
                    print("Sum Up all the expenses in a category")
                    expense_by_type = input("Write either (Food, Bills, Clothes, Phone or Other): ")
                    the_expenses_list = []
                    i = 0
                    j = 1
                    x = 2

                    while len(all_expenses) > i:
                        if all_expenses[i][x] == expense_by_type:
                            the_expenses_list.append(all_expenses[i][j])
                            i += 1
                        else:
                            i += 1

                    the_sum = sum_expenses(the_expenses_list)
                    print(the_sum)

                    if not exit_to_menu():
                        break

                elif options == "2":
                    print("This is the most expensive day -_-")
                    print(sum_expenses_by_day(all_expenses))

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
