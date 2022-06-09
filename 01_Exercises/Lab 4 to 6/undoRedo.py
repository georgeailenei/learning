# This file contains the functions that help to undo/redo a previous action.

def undo_repository(all_expenses, undo_list):
    """This function save the last element added in a list
    It returns a list"""
    i = len(all_expenses)
    j = len(undo_list)

    if i == 0:
        print("You cannot undo anymore")
    elif i > j:
        for element in range(i):
            undo_list.append(all_expenses[j])
            j += 1

    return undo_list

