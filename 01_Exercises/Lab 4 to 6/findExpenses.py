import removeExpenses


def find_greater_expenses(all_expenses, amount):
    """The function saves greater numbers than given by user.
    It returns a list of different elements"""
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
    """The function returns a list of elements of the same type"""
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
    """The function saves lower numbers than given by user.
    It returns a list of different elements"""
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
    """The function returns the location of a date in a list.
    It returns indexes for those dates"""
    dates = removeExpenses.get_date(all_expenses)
    check_if_date_used = []
    locations = []

    for date in dates:
        if date not in check_if_date_used:
            locations.append(dates.index(date))
            check_if_date_used.append(date)

    return locations


def find_expenses_with_same_amount(all_expenses, amount):
    """The function save the expenses that have same amounts
    It returns a list with those expenses"""
    expenses = []
    amounts = 1

    for expense in all_expenses:
        if amount == expense[amounts]:
            expenses.append(expense)

    return expenses
