import datetime


def calculate_my_age(day, month, year):
    """
    Input your date of birth and this function will return the number of days you lived so far.
    :param day: must be an int depending on the month but not bigger than 31.
    :param month: must be an int between 1 - 12
    :param year: 1 - 9999
    :return: int (your number of days lived on this planet)
    day_in_each_month - the first item of the list is 0 days because month 0 does not exist.
    """

    days_in_each_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    current_year = datetime.date.today().year
    days_in_a_year = 365
    years_lived = (current_year - 1) - year
    days_lived_so_far = years_lived * days_in_a_year
    days_this_year = 0
    days_after_birth_month = 0

    while True:

        if day > 31:
            print("You must write the correct date")
            break
        elif month > 12:
            print("You must write the correct date")
            break
        elif year > 10000 or year == 0:
            print("You must write the correct date")
            break

        for count_days in range(month, len(days_in_each_month) - month):
            days_after_birth_month = days_after_birth_month + days_in_each_month[count_days]
        days_after_birth_month = days_after_birth_month - (days_in_each_month[month] - day)

        for count_days in range(month + 1):
            days_this_year = days_this_year + days_in_each_month[count_days]
        days_this_year = days_this_year + day

        total_days_lived = days_lived_so_far + days_after_birth_month + days_this_year
        return total_days_lived


print(calculate_my_age(8, 1, 1996))

