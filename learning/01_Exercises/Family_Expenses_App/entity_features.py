from repository import memory


class EntityFeatures:
    def __init__(self, expenses, data_collected):
        self.expenses = expenses
        self.data_collected = data_collected

    def save_higher_expenses(self):
        """The function save the higher expenses than the input
        It returns a list with those expenses"""
        expenses_found = []
        _amount = 1

        for expense in self.expenses:
            the_expense = expense.split()
            if int(the_expense[_amount]) >= int(self.data_collected):
                expenses_found.append(expense)
        return expenses_found

    def save_expenses_with_same_amount(self):
        """The function save the expenses that have same amounts
        It returns a list with those expenses"""
        expenses_found = []
        amounts = 1

        for expense in self.expenses:
            the_expense = expense.split()

            if self.data_collected == the_expense[amounts]:
                expenses_found.append(expense)
        return expenses_found

    def sum_expenses_by_type(self):
        """The function returns the sum of expenses for a specific expense type
        It returns an integer that represents the sum of the expenses requested"""
        expenses_found = []
        i = 0
        j = 1
        x = 2

        while len(self.expenses) > i:
            expense = self.expenses[i].split()

            if expense[x] == self.data_collected:
                expenses_found.append(expense[j])
                i += 1
            else:
                i += 1
        return SingleDataFeatures(self.expenses).sum_expenses(expenses_found)

    def find_expenses_by_type(self):
        """The function returns a list of elements of the same type"""
        expenses_found = []
        i = 0
        j = 2

        while len(self.expenses) > i:
            expense = self.expenses[i].split()

            if expense[j] == self.data_collected:
                expenses_found.append(" ".join(expense))
                i += 1
            else:
                i += 1
        return expenses_found

    def find_greater_expenses(self):
        """The function saves greater numbers than given by user.
        It returns a list of different elements"""
        expenses_found = []
        i = 0
        j = 1

        while len(self.expenses) > i:
            expense = self.expenses[i].split()

            if int(expense[j]) > int(self.data_collected):
                expenses_found.append(" ".join(expense))
                i += 1
            else:
                i += 1
        return expenses_found


class SingleDataFeatures:
    def __init__(self, expenses):
        self.expenses = expenses

    def get_date(self):
        """This function returns a list with dates from expenses"""
        list_with_dates = []
        i = 0

        for expense in self.expenses:
            the_expense = expense.split()
            date = the_expense[i]
            list_with_dates.append(date)
        return list_with_dates

    def get_day(self, the_date):
        """The function returns an int representing a day from a date"""
        the_day = [the_date[0], the_date[1]]

        for i in the_day:
            if i == "0":
                the_day.remove(i)
        return int("".join(the_day))

    def get_month(self, the_date):
        """The function returns a string that represents the month in date"""
        the_month = [the_date[3], the_date[4]]
        return "".join(the_month)

    def get_multi_days(self):
        """The function returns a list of int that represent days"""
        dates = self.get_date()
        days = []

        for date in dates:
            days.append(self.get_day(date))
        return days

    def sum_expenses_by_day(self, day):
        """The function returns the sum of expenses for a specific day
        It returns an int"""
        day_amounts = []
        date = 0
        amount = 1

        for expense in self.expenses:
            the_expense = expense.split()
            if day == self.get_day(the_expense[date]):
                day_amounts.append(the_expense[amount])
        return self.sum_expenses(day_amounts)

    def sum_expenses(self, amounts):
        """It returns an integer that represents the sum of something"""
        total = 0
        for amount in amounts:
            total = total + int(amount)
        return total

    def find_date_location(self):
        """The function returns the location of a date in a list.
        It returns indexes for those dates"""
        dates = SingleDataFeatures(self.expenses).get_date()
        check_if_date_used = []
        locations = []

        for date in dates:
            if date not in check_if_date_used:
                locations.append(dates.index(date))
                check_if_date_used.append(date)
        return locations

    def expensive_day(self):
        """The function takes the entire list of expenses and finds the most expensive day
        It returns a string/message, but it doesn't consider the month. Consider fixing it."""
        dates = SingleDataFeatures(self.expenses).get_date()
        days = SingleDataFeatures(self.expenses).get_multi_days()
        check_if_day_used = []
        list_with_amounts = []
        i = 0

        while len(self.expenses) > i:
            if days[i] == SingleDataFeatures(self.expenses).get_day(dates[i]) and days[i] not in check_if_day_used:
                list_with_amounts.append(SingleDataFeatures(self.expenses).sum_expenses_by_day(days[i]))
                check_if_day_used.append(days[i])
                i += 1
            else:
                i += 1

        the_result = 0
        dates_locations = SingleDataFeatures(self.expenses).find_date_location()

        for amount in list_with_amounts:
            if the_result < amount:
                the_result = amount
        return f"\nThe most expensive day is {dates[dates_locations[list_with_amounts.index(the_result)]]} with a total of" \
               f" {the_result} spent"


class MultipleDataFeatures:
    def __init__(self, expenses, data_collected, data_collected_two):
        self.expenses = expenses
        self.data_collected = data_collected
        self.data_collected_two = data_collected_two

    def display_lower_expenses(self):
        """The function saves lower numbers than given by user.
        It returns a list of different elements"""
        expenses_found = []
        i = 0
        j = 0
        x = 1

        while len(self.expenses) > i:
            expense = self.expenses[i].split()

            if SingleDataFeatures(self.expenses).get_day(expense[j]) < SingleDataFeatures(self.expenses).get_day(self.data_collected):
                if int(self.data_collected_two) > int(expense[x]):
                    expenses_found.append(" ".join(expense))
                    i += 1
                else:
                    i += 1
            else:
                i += 1
        return expenses_found

    def remove_by_time_interval(self):
        the_dates = SingleDataFeatures(self.expenses).get_date()
        the_month = [SingleDataFeatures(self.expenses).get_month(self.data_collected), SingleDataFeatures(self.expenses).get_month(self.data_collected_two)]
        remove_from_day = SingleDataFeatures(self.expenses).get_day(self.data_collected)
        remove_to_day = SingleDataFeatures(self.expenses).get_day(self.data_collected_two)
        update_expenses = []
        i = 0

        if the_month[0] == the_month[1]:
            while len(self.expenses) > i:
                if remove_from_day <= SingleDataFeatures(self.expenses).get_day(the_dates[i]) <= remove_to_day:
                    i += 1
                else:
                    update_expenses.append(self.expenses[i])
                    i += 1
            memory.remove_all()
            memory.add_to_repository(update_expenses)
        else:
            print("The time interval is too long, please choose same month or subscribe to premium :))")
