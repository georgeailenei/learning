import os


def do_list_integers(random_nr):
    """
    :param: must be a random number or a string number.
    :return: a list of integers;
    :note: The function will fail if the string is not numeric;
    """
    random_nr = str(random_nr)
    random_list = list(random_nr)
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

    for num in random_list:
        if num in all_letters:
            return "This random number contains letters, please try again!"
        else:
            pass

    for num in range(len(random_list)):
        if random_list[num] == "-":
            random_list[num + 1] = int(random_list[num + 1]) * -1

    for num in random_list:
        if num == "-":
            random_list.remove(num)

    random_list = list(map(int, random_list))
    return random_list


assert do_list_integers("2234s") == "This random number contains letters, please try again!"
assert do_list_integers(-11) == [-1, 1]
assert do_list_integers("-11") == [-1, 1]
assert do_list_integers("23") == [2, 3]
assert do_list_integers(23) == [2, 3]


def find_prime_numbers(random_nr):
    """
    :param random_nr: must be a random number or a string number.
    :return: the prime numbers.
    """
    random_list = do_list_integers(random_nr)
    prime_numbers = []

    for num in random_list:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers


assert find_prime_numbers("234910") == [2, 3]
assert find_prime_numbers("-157384") == [5, 7, 3]
assert find_prime_numbers("-10245") == [2, 5]
assert find_prime_numbers("984132") == [3, 2]
assert find_prime_numbers("486") == []


def mountain_sequence_pattern(random_nr):
    """
    This function can take 5 numbers;
    :param random_nr: must be a random number or a string number.
    :return: FALSE OR TRUE - and - descriptive string.
    """
    random_list = do_list_integers(random_nr)
    sequence_one = 0
    sequence_two = 0

    if len(random_list) > 5 or len(random_list) < 5:
        return False

    for num in range(len(random_list) - 3):
        if random_list[num] + 1 == random_list[num + 1]:
            sequence_one += 1
        else:
            return False

    for other_num in range(2, len(random_list) - 1):
        if random_list[other_num] - 1 == random_list[other_num + 1]:
            sequence_two += 1
        else:
            return False

    if sequence_one == sequence_two:
        return True


assert mountain_sequence_pattern("234592") == False
assert mountain_sequence_pattern("-1010-1") == True
assert mountain_sequence_pattern("12321") == True
assert mountain_sequence_pattern("48238") == False
assert mountain_sequence_pattern("3") == False


def main_menu():
    """
    :return: A list of options/strings.
    """
    menu = ["Main Menu", "Option 1: To generate a list of integers input 1", "Option 2: To find prime numbers in a list input 2", "Option 3: To detect a mountain sequence number input 3"]

    for options in menu:
        print(options)

    return menu


def return_to_menu(menu_or_exit):
    """
    This function takes the user input to exit or to return to the main menu.
    """
    if menu_or_exit == "main menu":
        return main()
    else:
        print("You've exit the application")
        pass


def main():
    """
    This is the main function of the app which provides instructions and it takes a random number input.
    Examples:
        1213402
        -2-13-49 etc
    """
    main_menu()
    selected_option = input("Choose your option here: ")

    if selected_option == "1":
        os.system("cls")
        print("You've choose option 1: Generate a list of integers")
        user_input = input("Write some numbers and the app will convert it into a list of integers: ")
        user_result = do_list_integers(user_input)
        print("Output:")

        for num in user_result:
            print(num, end=" ")
        return user_result, return_to_menu(input("\nWrite main menu to return to it or exit: "))

    elif selected_option == "2":
        os.system("cls")
        print("You've choose option 2: Find prime numbers")
        user_input = input("Write some numbers and the app will find the prime numbers: ")
        user_result = find_prime_numbers(user_input)
        print("Output:")

        for num in user_result:
            print(num, end=" ")

        return user_result, return_to_menu(input("\nWrite main menu to return to it or exit: "))

    elif selected_option == "3":
        os.system("cls")
        print("You've choose option 3: Detect a mountain sequence number")
        user_input = input("Write 5 numbers to detect a mountain sequence number: ")
        user_result = mountain_sequence_pattern(user_input)
        print("Result:")
        if user_result:
            print("The app detected a mountain sequence number")
        else:
            print("This number does NOT represent a mountain sequence number")
        return user_result, return_to_menu(input("\nWrite main menu to return to it or exit: "))


if __name__ == "__main__":
    main()
