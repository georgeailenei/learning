import random
import os


#   Choose a random word.   - Completed.
def generate_a_word():
    a_random_list_of_names = ["robert", "dan", "coco", "george", "ioana"]
    return random.choice(a_random_list_of_names)  # this function returns a random string.


# Arrange arena. - Completed.
def print_hangman(number_of_mistakes, check_word):
    hangman_to_display_options = [
        ["   ______  ", "  |      | ", "  |      ", "  |     ", "  |     ", "__|__"],
        ["   ______  ", "  |      | ", "  |      o", "  |     ", "  |     ", "__|__"],
        ["   ______  ", "  |      | ", "  |      o", "  |      |", "  |     ", "__|__"],
        ["   ______  ", "  |      | ", "  |      o", "  |     ~|", "  |     ", "__|__"],
        ["   ______  ", "  |      | ", "  |      o", "  |     ~|~", "  |     ", "__|__"],
        ["   ______  ", "  |      | ", "  |      o", "  |     ~|~", "  |     |", "__|__"],
        ["   ______  ", "  |      | ", "  |      o", "  |     ~|~", "  |     | |", "__|__"],
    ]

    hangman_to_display = hangman_to_display_options[number_of_mistakes]

    for line in hangman_to_display:
        print(line)

    print("\n", "".join(check_word))  # The missing letters.

    return hangman_to_display  # this function returns a list of strings.


#   Print letters from the unknown word. - completed.
def get_word_with_spaces(the_random_word, letter):
    random_list = list(the_random_word)
    another_random_list = []

    for element in range(len(the_random_word)):
        if letter == random_list[element]:
            another_random_list.append(letter)
        else:
            another_random_list.append('_')
    return "".join(another_random_list)  # this functions returns a string.


#   If the letter is true. - Completed.
def word_contains_letter(the_random_word, letter):
    for c in range(len(the_random_word)):
        if letter == the_random_word[c]:
            return True
    return False


#   It finds the letter index.
def find_index(test):
    index_list = []
    for element in range(len(test)):
        if test[element] != "_":
            index_list.append(element)
    return index_list  # this function returns a list of int.


# You win. - Completed
def is_win(check):
    if "_" not in check:
        print("You are a damn winner, congratulations")
        return True


def letter_used(the_random_word, letter):
    if letter in list(the_random_word):
        return True
    return False


#   Welcome the player. - Completed.
def welcome_the_player():
    print("Welcome to the Hangman Game")

    do_you_wanna_play = None
    while True:
        do_you_wanna_play = input("Would you like to play? (Yes/NO) : ")

        if do_you_wanna_play in ('yes', 'no', 'YES', 'NO'):
            break

        print("Don't try to be smart, te-ai prajit?")

    if do_you_wanna_play == "Yes" or do_you_wanna_play == "yes":
        return True
    elif do_you_wanna_play == "No" or do_you_wanna_play == "no":
        print("Maybe some other time then, du-te tare.")
        return False


def main():
    start_game = welcome_the_player()
    the_random_word = generate_a_word()
    check_word = list(len(the_random_word) * '_')
    list_of_wrong_letters = []
    number_of_mistakes = 0

    while start_game:
        os.system("cls")

        print_hangman(number_of_mistakes, check_word)  # The arena.
        print("Below are the wrong letters, do not use them again.")
        print(list_of_wrong_letters)

        if is_win(check_word):
            break

        chosen_letter = input("\n" + "Choose a letter here: ")
        if word_contains_letter(the_random_word, chosen_letter) and letter_used(check_word, chosen_letter) == False:
            word_with_spaces = get_word_with_spaces(the_random_word, chosen_letter)
            correct_index = find_index(word_with_spaces)
            for position in correct_index:
                check_word[position] = word_with_spaces[position]
        elif number_of_mistakes < 6 and letter_used(list_of_wrong_letters, chosen_letter) == False and letter_used(check_word, chosen_letter) == False:
            number_of_mistakes += 1
            list_of_wrong_letters.append(chosen_letter)
        elif number_of_mistakes == 6:
            print("You lost, go cry!")
            break


main()
