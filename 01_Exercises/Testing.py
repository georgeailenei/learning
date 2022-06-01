def exit_to_menu():
    """It returns False or True depending on the input"""
    option = input("Do you want to continue? ")

    if option == "no" or option == "No":
        return False
    else:
        return True


print(exit_to_menu())