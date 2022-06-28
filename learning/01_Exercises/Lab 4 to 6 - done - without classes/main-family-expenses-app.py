import removeExpenses
import findExpenses
import repository
from interface import UI
import reports
import os


def main():
    all_expenses = []

    while True:

        app_interface = UI()
        app_interface.main_menu()
        # options.choose_option()

        # if options == "1":  # add expenses
        #     while True:
        #         os.system("cls")
        #         print("Please write your expense")
        #         display_all_expenses.display_expense(all_expenses)
        #
        #         data_collected = interface.UI().collect_data()
        #         data_collected_details = data_collected.get_all_expense_details()
        #         display_data = " ".join(data_collected_details)
        #
        #         if repository.check_all_data(data_collected):
        #             all_expenses.append(data_collected_details)
        #             print(f"The expense - {display_data} - has been added to the list")
        #         else:
        #             print("Please try to input your data again!")
        #
        #         if not exit_menu.exit_to_menu:
        #             break

        # elif options == "2":  # update expenses
        #     while True:
        #         os.system("cls")
        #         print("Please choose the expense that you want to update")
        #         interface.display_expense(all_expenses)
        #         update_the_expense = collect_data()
        #         update_expense_details = update_the_expense.get_all_expense_details()
        #
        #         if update_expense_details in all_expenses:
        #             expense_location = all_expenses.index(update_expense_details)
        #             all_expenses.remove(update_expense_details)
        #
        #             while True:
        #                 print("\nUpdate your expense")
        #                 update_the_expense = collect_data()
        #
        #                 if repository.check_all_data(update_the_expense):
        #                     all_expenses.insert(expense_location, update_the_expense.get_all_expense_details())
        #                     break
        #                 else:
        #                     print("Please try to input your data again!")
        #
        #         else:
        #             print("We could not find your expense, try again!")
        #
        #         print("\nUpdated list")
        #         interface.display_expense(all_expenses)
        #
        #         if not interface.exit_to_menu():
        #             break
        #
        # elif options == "3":  # Remove submenu
        #     while True:
        #         user_interface.submenu("Remove")
        #         options = interface.choose_option()
        #
        #         if options == "1":
        #             while True:
        #                 print("\nYou can now remove and expense by inserting the Date")
        #                 interface.display_expense(all_expenses)
        #
        #                 date_of_expense = input("Date (dd-mm-yy): ")
        #                 check_date = repository.Expense(date_of_expense, "", "")
        #
        #                 if check_date.check_date_format():
        #                     all_expenses = removeExpenses.remove_expense(all_expenses, date_of_expense)
        #                     print("\nUpdated list")
        #                     interface.display_expense(all_expenses)
        #                 else:
        #                     print("Please try to use the date format (dd-mm-yy)")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "2":
        #             while True:
        #                 print("\nYou can now remove expense by inserting the type/category")
        #                 interface.display_expense(all_expenses)
        #
        #                 expense_type = input("Type (Food, Bills, Clothes, Phone or Other): ")
        #                 check_type = repository.Expense("", "", expense_type)
        #
        #                 if check_type.check_type():
        #                     all_expenses = removeExpenses.remove_expense(all_expenses, expense_type)
        #                     print("\nUpdated list")
        #                     interface.display_expense(all_expenses)
        #                 else:
        #                     print("The app does not contain that type of expenses")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "3":
        #             while True:
        #                 print("\nYou can now remove expense by time interval")
        #                 interface.display_expense(all_expenses)
        #
        #                 from_day = input("From Date (dd-mm-yy): ")
        #                 to_day = input("To Date (dd-mm-yy): ")
        #                 dates = [repository.Expense(from_day, "", ""), repository.Expense(to_day, "", "")]
        #
        #                 if dates[0].check_date_format() and dates[1].check_date_format():
        #                     if dates[0].check_day_format() and dates[1].check_day_format():
        #                         all_expenses = removeExpenses.remove_by_time_interval(all_expenses, from_day, to_day)
        #                         print("\nUpdated list")
        #                         interface.display_expense(all_expenses)
        #                 else:
        #                     print("\nPlease try to input a date again.\n")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "4":
        #             break
        #
        # elif options == "4":    # Prints all expenses
        #     print("\nThis is your list of expenses:")
        #     interface.display_expense(all_expenses)
        #
        #     if not interface.exit_to_menu():
        #         continue
        #
        # elif options == "5":    # Search for expenses
        #     while True:
        #         print("\nYou can now search for expenses")
        #         user_interface.submenu("Search")
        #         options = interface.choose_option()
        #
        #         if options == "1":
        #             while True:
        #                 print("\nDisplay higher expenses\n")
        #                 interface.display_expense(all_expenses)
        #
        #                 amount = input("\nWrite amount: ")
        #                 check_amount = repository.Expense("", amount, "")
        #
        #                 if check_amount.check_amount():
        #                     interface.display_expense(findExpenses.find_greater_expenses(all_expenses, amount))
        #                 else:
        #                     print("\nPlease insert a number not random things.")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "2":
        #             while True:
        #                 print("\nPrint expenses by type\n")
        #                 interface.display_expense(all_expenses)
        #
        #                 expense_type = input("\nWrite type (Food, Bills, Clothes, Phone or Other): ")
        #                 check_type = repository.Expense("", "", expense_type)
        #
        #                 if check_type.check_type():
        #                     interface.display_expense(findExpenses.find_expenses_by_type(all_expenses, expense_type))
        #                 else:
        #                     print("\nThe apps does not contain that category")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "3":
        #             while True:
        #                 print("\nChoose a day and amount to print a list with smaller amounts from previous days\n")
        #                 interface.display_expense(all_expenses)
        #
        #                 amount = input("\nWrite amount: ")
        #                 expense_date_day = input("Write day (dd): ")
        #
        #                 check_amount = repository.Expense("", amount, "")
        #                 check_date = repository.Expense(expense_date_day, "", "")
        #
        #                 if check_date.check_day_format() and check_amount.check_amount():
        #                     interface.display_expense(
        #                         findExpenses.display_lower_expenses(all_expenses, expense_date_day, amount))
        #                 else:
        #                     print("\nWrong inputs, please try again!")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "4":
        #             break
        #
        # elif options == "6":    # Reports submenu
        #     while True:
        #         print("\nReports\n")
        #         user_interface.submenu("Reports")
        #         options = interface.choose_option()
        #
        #         if options == "1":
        #             while True:
        #                 print("Sum Up all the expenses in a category")
        #                 interface.display_expense(all_expenses)
        #
        #                 expense_type = input("Category (Food, Bills, Clothes, Phone or Other): ")
        #                 check_expense_type = repository.Expense("", "", expense_type)
        #
        #                 if check_expense_type.check_type():
        #                     print(f"\nThe sum for {expense_type} category is: {reports.sum_expenses_by_type(all_expenses, expense_type)}")
        #                 else:
        #                     print("The app does not contain that category")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "2":
        #             while True:
        #                 print("The current list of expenses")
        #                 interface.display_expense(all_expenses)
        #
        #                 print(reports.expensive_day(all_expenses))
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "3":
        #             while True:
        #                 print("\nThe current list of expenses")
        #                 interface.display_expense(all_expenses)
        #
        #                 amount = input("\nAmount: ")
        #                 check_amount = repository.Expense("", amount, "")
        #
        #                 if check_amount.check_amount():
        #                     print(f"\nThis is the list which contains the amount of {amount}:")
        #                     interface.display_expense(findExpenses.find_expenses_with_same_amount(all_expenses, amount))
        #                 else:
        #                     print("Please try to input an amount, nothing else")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "4":
        #             while True:
        #                 print("\nPrint all the expenses by category")
        #                 interface.display_expense(all_expenses)
        #
        #                 expense_type = input("Category (Food, Bills, Clothes, Phone or Other): ")
        #                 check_expense_type = repository.Expense("", "", expense_type)
        #
        #                 if check_expense_type.check_type():
        #                     print(f"\nThis is the full list of category {expense_type}:")
        #                     interface.display_expense(findExpenses.find_expenses_by_type(all_expenses, expense_type))
        #                 else:
        #                     print(f"This {expense_type} category does not exist, please try again\n")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "5":
        #             break
        #
        # elif options == "7":    # Filters submenu
        #     while True:
        #         print("\nFilters")
        #         user_interface.submenu("Filters")
        #         options = interface.choose_option()
        #
        #         if options == "1":
        #             while True:
        #                 print("\nYou can now remove all the expenses by category")
        #                 interface.display_expense(all_expenses)
        #
        #                 expense_type = input("Category (Food, Bills, Clothes, Phone or Other): ")
        #                 check_expense_type = repository.Expense("", "", expense_type)
        #
        #                 if check_expense_type.check_type():
        #                     all_expenses = removeExpenses.remove_expense(all_expenses, expense_type)
        #                     print(f"\nThe expenses from {expense_type} category has been removed")
        #                     print("New list of expenses:")
        #                     interface.display_expense(all_expenses)
        #                 else:
        #                     print(f"This {expense_type} category does not exist, please try again\n")
        #
        #                 if not interface.exit_to_menu():
        #                     break
        #
        #         elif options == "2":
        #             print("You can now remove all the smaller expenses")
        #             interface.display_expense(all_expenses)
        #
        #             amount = input("Amount: ")
        #             check_amount = repository.Expense("", amount, "")
        #
        #             if check_amount.check_amount():
        #                 all_expenses = removeExpenses.remove_expense_by_amount(all_expenses, amount)
        #                 print(f"\nExpenses which were less than {amount} has been removed")
        #                 print("New list of expenses:")
        #                 interface.display_expense(all_expenses)
        #             else:
        #                 print(f"This {amount} does not represent a number, please try again\n")
        #
        #             if not interface.exit_to_menu():
        #                 break
        #
        #         elif options == "3":
        #             break
        #
        # elif options == "8":    # Undo
        #     print("\nUndo")
        #     print("Are you sure that you want to go back in time? ")
        #
        #     if not interface.exit_to_menu():
        #         continue
        #
        # elif options == "9":  # exit app
        #     break
        #

if __name__ == '__main__':
    main()
