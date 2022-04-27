import os


def generate_int_list(random_nr):
    """
    :param: must be a random numbers separated by spaces.
    :return: a list of integers;
    :note: The function will fail if the string is not numeric;
    """

    strings_to_convert = []
    a = 0
    b = 0

    while a < len(random_nr):
        if random_nr[a] == " ":
            strings_to_convert.append(random_nr[b: a])
            b = a + 1
        a += 1
    strings_to_convert.append(random_nr[b: a])

    converted_int_list = []

    for i in strings_to_convert:
        try:
            converted_int_list.append(int(i))
        except ValueError:
            return "This random number contains characters that are not supported!"

    return converted_int_list


assert generate_int_list("22 1 -2") == [22, 1, -2]
assert generate_int_list("-3 12 14") == [-3, 12, 14]
assert generate_int_list("0 1 -23 $") == "This random number contains characters that are not supported!"


def list_the_prime_numbers(random_nr):
    """
    :param random_nr: must be random string numbers divided by space.
    Example: "22 1 3 11"
    :return: the prime numbers.
    """

    random_list = generate_int_list(random_nr)

    for element in random_list:
        try:
            element == int(element)
        except ValueError:
            return "This random number contains characters that are not supported!"

    prime_numbers = []

    for num in random_list:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers


assert list_the_prime_numbers("22 1 3 11") == [3, 11]
assert list_the_prime_numbers("0 5 11 40") == [5, 11]
assert list_the_prime_numbers("0 3 $") == "This random number contains characters that are not supported!"


def detect_the_longest_prime_nr_sequence(random_nr):
    """
    :param random_nr: must be random string numbers divided by space.
    Example: "22 1 3 11"
    :return: The longest sequence with prime numbers.
    """
    # 1 3 5 22 10 3 5 11
    # it must print 3 5 1 because is the longest sequence of prime numbers.
    # - 1 2 - - 5 6 7
    # a list with multiple lists where to store the sequences and then print the longest.

    list_of_integers = generate_int_list(random_nr)
    the_prime_numbers = list_the_prime_numbers(random_nr)
    prime_numbers_sequences = []
    the_sequence = []
    i = 0
    j = 0

    while i < len(list_of_integers):
        if list_of_integers[i] == the_prime_numbers[j]:
            the_sequence.append(list_of_integers[i])
            i += 1
            j += 1
        elif list_of_integers[i] != the_prime_numbers[j]:
            i += 1

    return prime_numbers_sequences


print(detect_the_longest_prime_nr_sequence("7 13 20 22 3 5"))

#
# def main_menu():
#     """
#     :return: A list of options/strings.
#     """
#     menu = ["Main Menu", "Option 1: To generate a list of integers input 1", "Option 2: To find prime numbers in a list input 2", "Option 3: To detect a mountain sequence number input 3"]
#
#     for options in menu:
#         print(options)
#
#     return menu
#
#
# def return_to_menu():
#     """
#     This function takes the user input to exit or to return to the main menu.
#     """
#     the_chosen_option = input("\n" "Write main menu to return to it or exit: ")
#
#     if the_chosen_option == "main menu":
#         return main()
#     else:
#         print("You've exit the application")
#         pass
#
#
# def main():
#     """
#     This is the main function of the app which provides instructions and it takes a random number input.
#     Examples:
#         1213402
#         -2-13-49 etc
#     """
#     main_menu()
#     selected_option = input("Choose your option here: ")
#
#     if selected_option == "1":
#         os.system("cls")
#         print("You've choose option 1: Generate a list of integers")
#         user_input = input("Write your numbers here: ")
#         user_result = generate_int_list(user_input)
#         print("Output:")
#
#         for num in user_result:
#             print(num, end=" ")
#
#         return_to_menu()
#
#     elif selected_option == "2":
#         os.system("cls")
#         print("You've choose option 2: Find prime numbers")
#         user_input = input("Write your numbers here: ")
#         user_result = find_prime_numbers(user_input)
#         print("Output:")
#
#         for num in user_result:
#             print(num, end=" ")
#
#         return_to_menu()
#
#     elif selected_option == "3":
#         os.system("cls")
#         print("You've choose option 3: Detect a mountain sequence number")
#         user_input = input("Write 5 numbers here: ")
#         user_result = mountain_sequence_pattern(user_input)
#         print("Result:")
#         if user_result:
#             print("The app detected a mountain sequence number")
#         else:
#             print("This number does NOT represent a mountain sequence number")
#         return_to_menu()
#
#
# if __name__ == "__main__":
#     main()
