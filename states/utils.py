import curses

# Global variables
row_counter = 0

def reset_row_counter():
    global row_counter
    row_counter = 0

def printRow(stdscr, text, capture_input=False, default_value=""):
    global row_counter
    try:
        stdscr.addstr(row_counter, 0, text)
        if capture_input:
            stdscr.addstr(row_counter, len(text), default_value)
            result = stdscr.getstr(row_counter, len(text), curses.COLS - len(text)).decode('utf-8')
            row_counter += 1
            return result
        stdscr.refresh()
    except curses.error:
        pass
    row_counter += 1
    return None