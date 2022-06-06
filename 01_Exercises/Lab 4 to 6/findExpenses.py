import removeExpenses

# Search for expenses
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
