from interface import ConsoleUI
from repository import memory
from control import Controller


def main():
    controller = Controller(memory)
    user_interface = ConsoleUI(controller)
    user_interface.start()


if __name__ == "__main__":
    main()
