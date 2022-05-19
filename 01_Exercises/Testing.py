# Just testing, nothing else.

expense_list = [["23-04-1992", "50", "Other"], ["25-04-1992", "34", "Other"], ["23-04-1992", "50", "Bills"]]
random_str_list = expense_list[0][0].strip()


def check_expense_by_day(the_date): # remove this functions cos you have in the main doc.
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


def expensive_day_list(all_expenses):
    """This function returns a list with all the dates from the all expenses"""
    expenses_by_day_list = []
    i = 0

    for expense in all_expenses:
        expenses_by_day_list.append(check_expense_by_day(expense[i]))

    return expenses_by_day_list


def find_expense_per_day(all_expenses):
    """This functions returns the sum of expenses for a day"""
    date_list = expensive_day_list(all_expenses)
    the_expenses = []

    i = 0
    j = 0
    x = 0
    y = 1

    while len(date_list) > i:
        if str(date_list[j]) in all_expenses[i][x] and i != len(date_list):
            the_expenses.append(all_expenses[i][y])
            i += 1
        elif str(date_list[j]) not in all_expenses[i][x] and i != len(date_list):
            i += 1
        else:
            i = 0
            j += 1




