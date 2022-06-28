import os
from consoleUI import ConsoleUI
from control import Controller


def dashboard():
    controller = Controller()
    user_interface = ConsoleUI(controller)
    user_interface.start()


if __name__ == '__main__':
    dashboard()
