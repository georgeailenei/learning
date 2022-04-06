def find_index(test):
    index_list = []
    for element in range(len(test)):
        if test[element] != "_":
            index_list.append(element)
            print(type(index_list[0]))
    return index_list


name = "__r_"
print(find_index(name))
print(type(find_index(name[0])))

