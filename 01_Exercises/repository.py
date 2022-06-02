class Expense:
    def __init__(self, date, amount, expense_type):  # the data that we're getting.
        self.date = date
        self.amount = amount
        self.expense_type = expense_type

    def check_date(self):
        list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
        check_date = list(self.date)

        if check_date[2] == "-" and check_date[5] == "-":
            for i in check_date:
                if i not in list_of_numbers:
                    return False
                else:
                    return True
        else:
            return False

    def check_amount(self):
        list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        check_amount = list(self.amount)

        for i in check_amount:
            if i not in list_of_numbers:
                return False
            else:
                return True

    def check_type(self):
        expense_type_list = ["Food", "Bills", "Clothes", "Phone", "Other"]

        if self.expense_type in expense_type_list:
            return True
        else:
            return False

    def get_all_expense_details(self):  # print all the details date, amount and type.
        return (self.date + " " + str(self.amount) + " " + self.expense_type).split()
