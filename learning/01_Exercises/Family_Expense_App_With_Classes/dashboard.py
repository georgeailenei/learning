import os
from main import main
from consoleUI import ConsoleUI
from start import Start


def dashboard():
    while True:
        # The UI interface
        os.system("cls")
        user_interface = ConsoleUI()
        user_interface.main_menu()

        # Interacting with the UI
        start = Start(main(ConsoleUI())).chosen_option()

        # Stop App
        if start == "stop":
            break


if __name__ == '__main__':
    dashboard()
