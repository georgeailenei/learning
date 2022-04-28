
the_list = [1, 13, 22]
the_answer = []

for num in the_list:
    for i in range(1, len(the_list)):
        if num > the_list[i]:
            the_answer.append(num)
        else:
            the_answer.clear()
            the_answer.append(the_list[i])

print(the_answer)


