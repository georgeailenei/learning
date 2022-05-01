def generate_int_list(random_nr):
    """
    :param: must be a random numbers separated by spaces.
    :return: a list of integers;
    :note: The function will fail if the string is not numeric;
    """

    strings_to_convert = []
    a = 0
    b = 0

    while a < len(random_nr):
        if random_nr[a] == " ":
            strings_to_convert.append(random_nr[b: a])
            b = a + 1
        a += 1
    strings_to_convert.append(random_nr[b: a])

    converted_int_list = []

    for i in strings_to_convert:
        try:
            converted_int_list.append(int(i))
        except ValueError:
            return "This random number contains characters that are not supported!"

    return converted_int_list


def is_prime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def find_the_longest_prime_num_sequence(random_num):
    random_nr_list = generate_int_list(random_num)
    all_possible_sequences = []
    i = 0
    j = 0

    while j < len(random_nr_list):
        if i > len(random_nr_list):
            j += 1
            i = 0
        elif len(random_nr_list[j:i]) == 0:
            i += 1
        elif len(random_nr_list[j:i]) > 0:
            all_possible_sequences.append(random_nr_list[j:i])
            i += 1

    prime_num_sequences = []
    check_all_num_in_sequence = []
    i = 0
    j = 0

    while j < len(all_possible_sequences):
        if i == len(all_possible_sequences[j]):    # reset and check if all num were primes then move on.
            if len(check_all_num_in_sequence) == len(all_possible_sequences[j]):
                prime_num_sequences.append(all_possible_sequences[j][:])
                check_all_num_in_sequence.clear()
            j += 1
            i = 0
        elif is_prime(all_possible_sequences[j][i]):    # save the num in a new list to check the entire sequence
            check_all_num_in_sequence.append(all_possible_sequences[j][i])
            i += 1
        else:    # if num != prime num then clear the checking list, reset to the first el in list and move on
            check_all_num_in_sequence.clear()
            j += 1
            i = 0

    sequence_size = []
    for el in prime_num_sequences:      # find the length of each list.
        sequence_size.append(len(el))

    longest_sequence = 0

    for size in sequence_size:          # find the longest list
        if size > longest_sequence:
            longest_sequence = size

    for sequence in prime_num_sequences:    # find the longest sequence by comparing it matching it with the length.
        if len(sequence) == longest_sequence:
            return sequence


assert find_the_longest_prime_num_sequence("11 7 5 3 5 10 20 40 2 15 11 13 2") == [11, 7, 5, 3, 5]
assert find_the_longest_prime_num_sequence("2 3 5 10") == [2, 3, 5]
assert find_the_longest_prime_num_sequence("2 3 5 7 11 13 20 50 3 2 100") == [2, 3, 5, 7, 11, 13]
