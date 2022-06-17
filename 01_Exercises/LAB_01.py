# LAB 1
# Calculati suma a N numere naturale.
def sum_numbers(numbers):
    the_sum = 0
    found_negative_number = False

    for number in numbers:
        if number < 0:
            found_negative_number = True
        else:
            the_sum = the_sum + number

    if found_negative_number:
        print("Choose only natural numbers")
    else:
        return the_sum


# print(sum_numbers([2, 3]))


# Verificați daca un număr citit de la tastatura este prim.
def only_prime_numbers(number):
    divisors = []

    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)

    if number == 0 or number == 1:
        print("This is NOT a prime number")
    elif len(divisors) > 0:
        print("This is NOT a prime number")
    else:
        print("This is a prime number")


# only_prime_numbers(4)


# Calculați cel mai mare divizor comun a doua numere.
def highest_divisors(a, b):
    divisors_a = []
    divisors_b = []
    max_nr = -99999

    for i in range(1, a + 1):
        if a % i == 0:
            divisors_a.append(i)

    for y in range(1, b + 1):
        if b % y == 0:
            divisors_b.append(y)

    for a in divisors_a:
        for b in divisors_b:
            if a == b and a > max_nr:
                max_nr = a

    return max_nr


print(highest_divisors(10, 15))
