
class Expense:
    def __init__(self, date, amount, expense_type):
        self.id = None
        self.date = date
        self.amount = amount
        self.expense_type = expense_type

    def __repr__(self):
        return f'{self.id} {self.date} {self.amount} {self.expense_type}'


class ExpenseValidator:
    def check_date_format(self, date):
        """This method check if the format of the date is correct.
        And it returns a boolean"""
        list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        check_format = list(date)

        if len(check_format) <= 6:
            return False
        elif check_format[2] == "-" and check_format[5] == "-":
            for i in date:
                if i not in list_of_numbers:
                    return False
                else:
                    return True

    def check_day_format(self, date):
        """This method checks if the day given by the user relates to a real calendar
        Also, it returns a boolean"""
        dates = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
                 "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

        check_the_format = [date[0], date[1]]
        check_the_format = "".join(check_the_format)

        if check_the_format in dates:
            return True
        else:
            return False

    def check_month_format(self, date):
        """This method checks if the month given by the user relates to a real calendar
        Also, it returns a boolean"""
        dates = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        check_the_format = [date[3], date[4]]
        check_the_format = "".join(check_the_format)

        if check_the_format in dates:
            return True
        else:
            return False

    def check_year_format(self, date):
        """This method checks if the year given by the user relates to a real calendar
        Also, it returns a boolean"""
        check_the_format = []

        for i in range(6, len(date)):
            check_the_format.append(date[i])

        if len(check_the_format) > 4:
            return False
        elif check_the_format[0] == "0":
            return False
        else:
            return True

    def check_amount(self, amount):
        """This method checks if the amount given by the user relates to a number"""
        list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        check_amount = list(amount)

        for i in check_amount:
            if i not in list_of_numbers:
                return False
            else:
                return True

    def check_amount_int(self, amount):
        """This method checks doesn't allow 0 to be in front of any number.
        Also, it returns a boolean"""
        the_amount = list(amount)

        if the_amount[0] == "0":
            return False
        else:
            return True

    def check_type(self, expense_type):
        """The method checks if the user input is right.
        It returns a boolean."""
        expense_type_list = ["Food", "Bills", "Clothes", "Phone", "Other"]

        if expense_type in expense_type_list:
            return True
        else:
            return False

    def validate(self, expense):
        return (
                self.check_date_format(expense.date)
                and self.check_amount(expense.amount)
                and self.check_type(expense.expense_type)
                and self.check_day_format(expense.date)
                and self.check_month_format(expense.date)
                and self.check_year_format(expense.date)
                and self.check_amount_int(expense.amount)
        )
