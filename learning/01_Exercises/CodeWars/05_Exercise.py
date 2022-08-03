# def top_3_words(text):
#     words = []
#
#     for letter in text:
#         if letter.isalpha() or letter == "'" or letter == " ":
#             words.append(letter)
#
#     words = "".join(words).strip().lower()
#     words = words.split()
#
#     commas = ["'", "''", "'''", "''''", "'''''", "''''''"]
#     for word in words:
#         if word in commas:
#             words = []
#
#     if len(words) == 0:
#         return []
#     elif len(words) < 3:
#         return words
#     elif len(words) >= 3:
#         topWords = {}
#         for word in words:
#             topWords[word] = words.count(word)
#
#         counts = [value for value in topWords.values()]
#         counts.sort(), counts.reverse()
#
#         return sorted(topWords, key=topWords.get, reverse=True)[:3]
#
# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# top_3_words("a a a  b  c c  d d d d  e e e e e")
# top_3_words("  //wont won't won't ")
# top_3_words("  , e   .. ")
# top_3_words("  ...  ")
# top_3_words("  '  ")
# top_3_words("  '''  ")
# top_3_words("spwlgogdke")
#

def findNumber(num):
    randomNumbers = [2, 9, 23, 55, 12, 15, 21, 85, 20, 5]
    randomNumbers.sort()

    count = int(len(randomNumbers) / 2)
    answer = None

    step = 1
    i = 0
    while answer is None:
        print(f"Step nr: {step}")
        step += 1
        if num in randomNumbers[i:count]:
            return "FOUND"
        else:
            i = count
            count = count + int(count / 2)

print(findNumber(21))
