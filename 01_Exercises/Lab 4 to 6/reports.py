import removeExpenses
import findExpenses

# Functions for the submenu - Reports
def sum_expenses(amounts):
    total = 0

    for amount in amounts:
        total = total + int(amount)

    return total


def sum_expenses_by_type(all_expenses, expense_type):
    expenses = []
    i = 0
    j = 1
    x = 2

    while len(all_expenses) > i:
        if all_expenses[i][x] == expense_type:
            expenses.append(all_expenses[i][j])
            i += 1
        else:
            i += 1

    return sum_expenses(expenses)


def sum_expenses_by_day(all_expenses, day):
    day_amounts = []
    date = 0
    amount = 1

    for expense in all_expenses:
        if day == removeExpenses.get_day(expense[date]):
            day_amounts.append(expense[amount])

    return sum_expenses(day_amounts)


def expensive_day(all_expenses):
    dates = removeExpenses.get_date(all_expenses)
    days = removeExpenses.get_multi_days(all_expenses)
    check_if_day_used = []
    list_with_amounts = []
    i = 0

    while len(all_expenses) > i:
        if days[i] == removeExpenses.get_day(dates[i]) and days[i] not in check_if_day_used:
            list_with_amounts.append(sum_expenses_by_day(all_expenses, days[i]))
            check_if_day_used.append(days[i])
            i += 1
        else:
            i += 1

    the_result = 0
    dates_locations = findExpenses.find_date_location(all_expenses)

    for amount in list_with_amounts:
        if the_result < amount:
            the_result = amount

    return f"\nThe most expensive day is {dates[dates_locations[list_with_amounts.index(the_result)]]} with a total of" \
           f" {sum_expenses_by_day(all_expenses, days[dates_locations[list_with_amounts.index(the_result)]])} spent"
