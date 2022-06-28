"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords
( "This is a test") => returns "This is a test" spinWords
( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):
    random_letters = list(sentence)
    list_of_words = []
    i = 0
    j = 0

    while i < len(random_letters):
        if random_letters[i] == " ":
            list_of_words.append(random_letters[j:i])
            j = i + 1
            i += 1
        else:
            i += 1

    list_of_words.append(random_letters[j:i])
    spin_words_list = []

    for i in list_of_words:
        if len(i) >= 5:
            spin_words_list.append(i[::-1])
        else:
            spin_words_list.append(i)

    final_answer = []

    for i in spin_words_list:
        final_answer.append("".join(i))

    return " ".join(final_answer)


assert spin_words("Welcome") == "emocleW"
assert spin_words("to") == "to"
assert spin_words("CodeWars") == "sraWedoC"
assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"
