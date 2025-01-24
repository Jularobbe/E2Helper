import curses
import os
from datetime import datetime
from .state import State
from .utils import printRow, reset_row_counter

class SetupState(State):
    def run(self, stdscr):
        curses.echo()
        stdscr.clear()
        reset_row_counter()

        # Load existing values if available
        token, cookie, profile_url, last_saved = "", "", "", "Never"
        if os.path.exists('resources/storage.txt'):
            with open('resources/storage.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("token="):
                        token = line.split('=')[1].strip()
                    elif line.startswith("cookie="):
                        cookie = line.split('=')[1].strip()
                    elif line.startswith("profile_url="):
                        profile_url = line.split('=')[1].strip()
                    elif line.startswith("last_saved="):
                        last_saved = line.split('=')[1].strip()

        printRow(stdscr, f"Current token: {token}")
        printRow(stdscr, f"Current cookie: {cookie}")
        printRow(stdscr, f"Current profile URL: {profile_url}")
        printRow(stdscr, f"Last saved: {last_saved}")
        new_token = printRow(stdscr, "Enter new token: ", capture_input=True, default_value=token)
        new_cookie = printRow(stdscr, "Enter new cookie: ", capture_input=True, default_value=cookie)
        new_profile_url = printRow(stdscr, "Enter new profile URL: ", capture_input=True, default_value=profile_url)

        # Save new values only if they have changed
        if new_token != token or new_cookie != cookie or new_profile_url != profile_url:
            with open('resources/storage.txt', 'w') as f:
                f.write(f"token={new_token}\ncookie={new_cookie}\nprofile_url={new_profile_url}\nlast_saved={datetime.now()}\n")
            printRow(stdscr, "Values saved. Press Enter to return to menu...")
        else:
            printRow(stdscr, "No changes made. Press Enter to return to menu...")

        stdscr.getch()
        curses.noecho()
        return 'menu'
