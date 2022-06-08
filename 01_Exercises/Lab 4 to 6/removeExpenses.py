# Functions for the submenu - Remove Expenses
def remove_expense(all_expenses, requested_format):
    updated_expense = []

    for expense in all_expenses:
        if requested_format not in expense:
            updated_expense.append(expense)

    return updated_expense


def get_date(all_expenses):
    """This function returns the date from expenses"""
    list_with_dates = []
    i = 0

    for date in all_expenses:
        list_with_dates.append(date[i])

    return list_with_dates


def get_day(the_date):
    the_day = [the_date[0], the_date[1]]

    for i in the_day:
        if i == "0":
            the_day.remove(i)

    return int("".join(the_day))


def get_multi_days(all_expenses):
    dates = get_date(all_expenses)
    days = []

    for date in dates:
        days.append(get_day(date))

    return days

def get_month(the_date):
    the_month = [the_date[3], the_date[4]]
    return "".join(the_month)


def remove_expense_by_amount(all_expenses, amount):
    expenses = []

    for expense in all_expenses:
        if int(amount) <= int(expense[1]):
            expenses.append(expense)

    return expenses


def remove_by_time_interval(all_expenses, from_date, to_date):
    the_dates = get_date(all_expenses)
    the_month = [get_month(from_date), get_month(to_date)]
    remove_from_day = get_day(from_date)
    remove_to_day = get_day(to_date)
    updated_expenses_list = []
    i = 0

    # This app does not allow the user to remove expenses for more than a month.
    if the_month[0] == the_month[1]:
        while len(all_expenses) > i:
            if remove_from_day <= get_day(the_dates[i]) <= remove_to_day:
                i += 1
            else:
                updated_expenses_list.append(all_expenses[i])
                i += 1
    else:
        print("The time interval is too long, please choose same month or subscribe to premium :))")

    return updated_expenses_list
