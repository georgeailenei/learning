import datetime


def calculate_my_age(day, month, year):
    """
    Input: Day, Month and year - and this function will return how many days you lived on earth.
    Example: 23, 12, 1992
    """

    days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    current_day = datetime.date.today().day
    days_in_a_year = 365         # Every 4 years, a year has 366 days.
    years_lived = (current_year - 1) - year
    leap_year_days = int(years_lived / 4)   # Find how many additional days he/she lived.
    days_lived_first_year = 0
    days_lived_this_year = 0

    if year <= 0:
        return "Write your date of birth again"

    for days in range(month, len(days_in_each_month)):  # Days lived last year but not including the birthday month.
        days_lived_first_year = days_lived_first_year + days_in_each_month[days]

    for days in range(current_month - 1):   # Days lived this year but not including this month.
        days_lived_this_year = days_lived_this_year + days_in_each_month[days]

    days_lived_after_last_birthday = (days_lived_this_year + days_lived_first_year) + (days_in_each_month[month - 1] - day) + current_day
    total_days_lived = (days_in_a_year * years_lived) + days_lived_after_last_birthday + leap_year_days

    return total_days_lived


print(calculate_my_age(23, 4, 1992))
print(calculate_my_age(16, 12, 1989))
print(calculate_my_age(11, 11, 1996))
print(calculate_my_age(23, 4, 0))
print(calculate_my_age(23, 4, -1))


assert calculate_my_age(23, 4, 1992) == 10959
assert calculate_my_age(16, 12, 1989) == 11818
assert calculate_my_age(24, 4, 2022) == 1
assert calculate_my_age(23, 4, 2022) == 2
assert calculate_my_age(11, 11, 1996) == 9296
assert calculate_my_age(23, 4, -1) == "Write your date of birth again"
