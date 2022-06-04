# Functions for the submenu - Remove Expenses
def remove_expense(all_expenses, requested_format):
    updated_expense = []

    for expense in all_expenses:
        if requested_format not in expense:
            updated_expense.append(expense)

    return updated_expense
