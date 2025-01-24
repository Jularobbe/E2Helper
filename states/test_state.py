from .state import State
from .utils import printRow, reset_row_counter

class TestState(State):
    def run(self, stdscr):
        stdscr.clear()
        reset_row_counter()
        printRow(stdscr, "Hello World")
        printRow(stdscr, "Press Enter to return to menu...")
        stdscr.refresh()
        stdscr.getch()
        return 'menu'
