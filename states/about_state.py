from .state import State
from .utils import printRow, reset_row_counter

class AboutState(State):
    def run(self, stdscr):
        stdscr.clear()
        reset_row_counter()
        printRow(stdscr, "Hello and thank you for using E2Helper!")
        printRow(stdscr, "I wrote this basic Python program to help users with their E2 tasks.")
        printRow(stdscr, "Feel free to visit my E2 profile: https://app.earth2.io/#profile/4cab63ed-d54e-4e57-a202-1c8730aff35e")
        printRow(stdscr, "Use code 'resources' at checkout for a 7.5% discount on new land purchases if you like my work and would like to support me to make more great tools like this one :).")
        printRow(stdscr, "Press Enter to return to the menu...")
        stdscr.refresh()
        stdscr.getch()
        return 'menu'