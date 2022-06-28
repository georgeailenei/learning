def move_zeros(array):
    zeros_in_array = 0
    list_without_zeros = []

    for i in array:  # find how many zeros are in the array
        if i == 0:
            zeros_in_array += 1

    for j in range(len(array)):  # save all the numbers but zeros
        if array[j] == 0:
            continue
        else:
            list_without_zeros.append(array[j])

    for el in range(zeros_in_array):      # add all the zeros at the end of the list
        list_without_zeros.append(0)

    array = list_without_zeros

    return array
