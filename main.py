import curses
from states import MenuState, TestState, SetupState, QuitState, AboutState
from states.utils import reset_row_counter

# Global variables
stdscr = None

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

if __name__ == "__main__":
    sm = StateMachine()
    sm.add_state('menu', MenuState())
    sm.add_state('test', TestState())
    sm.add_state('setup', SetupState())
    sm.add_state('quit', QuitState())
    sm.add_state('about', AboutState())
    sm.set_state('menu')
    curses.wrapper(sm.run)
