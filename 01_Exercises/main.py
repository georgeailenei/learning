# LAB 1
# Calculati suma a N numere naturale.
def sum_numbers(*numbers):
    sum = 0
    find = 0

    for check in numbers:
        if check < 0:
            find = -1

    for num in numbers:
        sum = sum + num

    if find < 0:
        print("Choose only natural numbers")
    else:
        return sum


print(sum_numbers(-2, 3))


# Verificați daca un număr citit de la tastatura este prim.
def only_prime_numbers(number):
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    if number == 0 or number == 1:
        print("This is NOT a prime number")
    elif len(divisors) > 2:
        print("This is NOT a prime number")
    else:
        print("This is a prime number")


only_prime_numbers(13)


# Calculați cel mai mare divizor comun a doua numere.
def highest_divisors(a, b):
    divisors_a = []
    divisors_b = []
    highest_divisor = []

    for i in range(1, a):
        if a % i == 0:
            divisors_a.append(i)

    for y in range(1, b):
        if b % y == 0:
            divisors_b.append(y)

    while True:
        compare = 0
        if len(divisors_a) >= len(divisors_b):
            for find in range(len(divisors_a)):
                if divisors_a[find] == divisors_b[compare]:
                    highest_divisor.append(divisors_a[find])
                    compare = compare + 1

        elif len(divisors_b) >= len(divisors_a):
            for find in range(len(divisors_b)):
                if divisors_b[find] == divisors_a[compare]:
                    highest_divisor.append(divisors_b[find])
                    compare = compare + 1

        print("Cel mai mare divizor comun este " + str(highest_divisor[-1]))
        break


highest_divisors(10, 25)
