import removeExpenses

# Functions for the submenu - Find expenses
def find_greater_expenses(all_expenses, amount):
    expenses = []
    i = 0
    j = 1

    while len(all_expenses) > i:
        if int(all_expenses[i][j]) > int(amount):
            expenses.append(all_expenses[i])
            i += 1
        else:
            i += 1

    return expenses


def find_expenses_by_type(all_expenses, expense_type):
    expenses = []
    i = 0
    j = 2

    while len(all_expenses) > i:
        if all_expenses[i][j] == expense_type:
            expenses.append(all_expenses[i])
            i += 1
        else:
            i += 1

    return expenses


def display_lower_expenses(all_expenses, date_day, amount):
    expenses = []
    i = 0
    j = 0
    x = 1

    while len(all_expenses) > i:
        if removeExpenses.get_day(all_expenses[i][j]) < removeExpenses.get_day(date_day):
            if int(amount) > int(all_expenses[i][x]):
                expenses.append(all_expenses[i])
                i += 1
            else:
                i += 1
        else:
            i += 1

    return expenses


def find_date_location(all_expenses):
    dates = removeExpenses.get_date(all_expenses)
    check_if_date_used = []
    locations = []

    for date in dates:
        if date not in check_if_date_used:
            locations.append(dates.index(date))
            check_if_date_used.append(date)

    return locations


def find_expenses_with_same_amount(all_expenses, amount):
    expenses = []
    amounts = 1

    for expense in all_expenses:
        if amount == expense[amounts]:
            expenses.append(expense)

    return expenses
