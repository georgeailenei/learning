import removeExpenses

# Various functions for the report submenu
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


def expensive_day(all_expenses):
        days = removeExpenses.get_multi_days(all_expenses)
        amounts_to_sum = []
        i = 0
        j = 0
        k = 0
        x = 1

        while len(all_expenses) > i:
            if removeExpenses.get_day(all_expenses[i][j]) == days[k]:
                amounts_to_sum.append(all_expenses[i][x])
                i += 1
            elif i == len(days):
                amounts_to_sum.append("ceva")
                k += 1
                i = 0
            else:
                i += 1

        return amounts_to_sum

random_list = [["23-04-2022", "10", "Other"], ["12-04-2022", "10", "Other"], ["23-04-2022", "10", "Other"]]
print(expensive_day(random_list))
