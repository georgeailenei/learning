
randomMovie = "2 : Never Back Down | It tells the story of a frustrated and conflicted teenager. | Romance | None"
a = randomMovie.split()
print(a)

title = []
description = []
genre = []
count = 4

for word in range(count, len(randomMovie)):
    if randomMovie[word] != "|":
        title.append(randomMovie[word])
    else:
        count = randomMovie.index(randomMovie[word])
        break

title = "".join(title[:-1])
count += 1
print(title)
print(count)

for word in range(count, len(randomMovie)):
    if randomMovie[word] != "|":
        description.append(randomMovie[word])
    else:
        count = randomMovie.index(randomMovie[word])
        break

description = "".join(description[1:-1])
print(description)
print(count)

for word in range(count, len(randomMovie)):
    if randomMovie[word] != "|":
        genre.append(randomMovie[word])
    else:
        break

genre = "".join(genre[1:-1])
print(genre)




