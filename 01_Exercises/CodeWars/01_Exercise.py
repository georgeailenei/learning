# Exercise_01
def square_digits(num):
    """
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
    """

    list_of_num = list(str(num))
    list_of_square_num = []

    for i in list_of_num:
        square_num = int(i) * int(i)
        list_of_square_num.append(str(square_num))

    the_new_num = "".join(list_of_square_num)

    return int(the_new_num)


print(square_digits(923))


# Exercise_02
def get_count(sentence):
    """
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
    """
    list_of_vowels = ["a", "e", "i", "o", "u"]
    vowels_in_sentence = []
    sum = 0
    for vowels in list_of_vowels:
        if vowels in list(sentence):
            vowels_in_sentence.append(sentence.count(vowels))

    for i in vowels_in_sentence:
        sum = sum + i

    return sum


print(get_count("abracadabra"))
