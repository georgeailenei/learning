# def top_3_words(text):
#     allLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "'"]
#     symbol = ["'", "''", "'''", "''''", "'''''", "''''''"]
#     theListWithWords = text.split()
#     listsWithLetters = [list(word.lower()) for word in theListWithWords]
#
#     theListWithWordsUpdated = []
#     finalList = None
#     count = 0
#
#     while len(listsWithLetters) > count:
#         word = [letter for letter in listsWithLetters[count] if letter in allLetters]
#         theListWithWordsUpdated.append("".join(word).split())
#         lastCheck = ["".join(word) for word in theListWithWordsUpdated if word != []]
#         finalList = lastCheck
#         count += 1
#
#     finalCheck = [word for word in finalList if word not in symbol]
#     if not finalCheck:
#         return []
#
#     topThreeWords = []
#     checkedWords = []
#     countList = []
#
#     for word in finalCheck:
#         if word not in checkedWords:
#             countList.append(finalCheck.count(word))
#             checkedWords.append(word)
#
#     checker = 0
#
#     while True:
#         findNumber = max(countList) - checker
#         checker += 1
#
#         if findNumber in countList:
#             topThreeWords.append(checkedWords[countList.index(findNumber)])
#
#         if len(topThreeWords) == 3:
#             break
#         elif len(topThreeWords) == len(countList):
#             break
#
#     print(topThreeWords)
#
#
# # print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
# top_3_words("a a a  b  c c  d d d d  e e e e e")
# # top_3_words("  //wont won't won't ")
# # top_3_words("  '  ")
# # top_3_words("  ...  ")
# # top_3_words("  '''  ")
# # top_3_words("  , e   .. ")
