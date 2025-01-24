from .state import State
from .utils import printRow, reset_row_counter

class QuitState(State):
    def run(self, stdscr):
        stdscr.clear()
        reset_row_counter()
        printRow(stdscr, "Quitting...")
        stdscr.refresh()
        stdscr.getch()
        return None
