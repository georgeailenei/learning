"""
Scrieți o aplicație care gestionează cheltuielile de familie efectuate într-o lună.
Pentru o cheltuială se vor retine ziua (din luna), suma, tipul cheltuielii (5 categorii:
mâncare, întreținere, îmbrăcăminte, telefon, altele). Aplicația să permită
efectuarea repetată a următoarelor operații:
"""

"""
1. Adaugă cheltuială - This is the 1st task for today. 
• adaugă o nouă cheltuială (se specifică ziua, suma, tipul)
• actualizează cheltuială (se specifică ziua, suma, tipul)
"""


class Expense:
    def __init__(self, date, amount, expense_type):  # the data that we're getting.
        self.date = date
        self.amount = amount
        self.expense_type = expense_type

    def get_all_expense_details(self):  # print all the details date, amount and type.
        return self.date + " " + self.amount + " " + self.expense_type


class StoreExpenses:    # store and display the data.
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def display(self):
        return self.expenses


def main_menu():    # information about the app.
    print("This App allows you to store your expenses.")


def exit_menu():
    choose_option = input("Do you have more inputs to make or exit? ")
    return choose_option


def collect_data():     # collects the data and stores in as object.
    the_date_of_expense = input("Write the date of the expense: ")
    the_amount_of_expense = input("Write the amount of the expense: ")
    the_type_of_expense = input("Write the type (Food, Bills, Clothes, Phone or Other: ")
    return Expense(the_date_of_expense, the_amount_of_expense, the_type_of_expense)


def main():
    main_menu()
    all_expenses = []

    while True:
        data_collection = collect_data()
        all_expenses.append(data_collection.get_all_expense_details())
        print(all_expenses)     # display the current list of expenses.

        if exit_menu() == "exit":
            break
        else:
            continue


if __name__ == '__main__':
    main()
