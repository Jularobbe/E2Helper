import curses
from .state import State
from .utils import printRow, reset_row_counter

class MenuState(State):
    def run(self, stdscr):
        options = ["Test", "Setup", "About", "Quit"]
        current_selection = 0

        def draw_menu():
            nonlocal current_selection
            stdscr.clear()
            reset_row_counter()
            with open('resources/banner.txt', 'r') as f:
                banner = f.readlines()
            for line in banner:
                printRow(stdscr, line)
            printRow(stdscr, "-" * curses.COLS)
            printRow(stdscr, "\n")
            for i, option in enumerate(options):
                if i == current_selection:
                    printRow(stdscr, f"> {option}")
                else:
                    printRow(stdscr, f"  {option}")
            stdscr.refresh()

        while True:
            draw_menu()
            key = stdscr.getch()
            if key == curses.KEY_UP:
                current_selection = (current_selection - 1) % len(options)
            elif key == curses.KEY_DOWN:
                current_selection = (current_selection + 1) % len(options)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_selection == 0:
                    return 'test'
                elif current_selection == 1:
                    return 'setup'
                elif current_selection == 2:
                    return 'about'
                elif current_selection == 3:
                    return 'quit'
