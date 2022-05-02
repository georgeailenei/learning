"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples:
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    words = text.split()
    first_letter = []
    simbols = ["!", "?", ".", "-"]
    i = 0

    for letter in words:
        if letter not in simbols:
            first_letter.append(letter[i] + "ay") # Save all first letters and add "ay".
        else:
            first_letter.append(letter[i])

    words_and_letter = []

    for word in words: # convert the strings in list of letters.
        words_and_letter.append(list(word))

    for letter in words_and_letter:  # remove first letters from the lists.
        letter.pop(i)

    for i in range(len(words_and_letter)): # add first letters + "ay" at the end of the "word".
        if simbols not in words_and_letter:
            words_and_letter[i] = "".join(words_and_letter[i]) + first_letter[i]


    return " ".join(words_and_letter)


print(pig_it("Pig latin is cool !"))
