import curses
import os
import sys
import importlib
from states.utils import reset_row_counter

# Global variables
stdscr = None

# Determine the base path for resources
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, state):
        self.states[name] = state

    def set_state(self, name):
        self.current_state = self.states.get(name)
        reset_row_counter()

    def run(self, stdscr_instance):
        global stdscr
        stdscr = stdscr_instance
        while self.current_state:
            next_state_name = self.current_state.run(stdscr)
            self.set_state(next_state_name)

def main(stdscr):
    state_machine = StateMachine()
    
    # Dynamically import all state classes from the states folder
    states_folder = os.path.join(base_path, "states")
    for filename in os.listdir(states_folder):
        if filename.endswith(".py") and filename != "__init__.py" and filename != "utils.py":
            module_name = f"states.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and attr_name.endswith("State"):
                    state_machine.add_state(attr_name.lower().replace("state", ""), attr(state_machine))

    state_machine.set_state("menu")
    state_machine.run(stdscr)

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")  # Keep the console window open
