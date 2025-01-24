import os
import sys

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

class State:
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.banner_path = os.path.join(base_path, "resources", "banner.txt")
        self.storage_path = os.path.join(base_path, "resources", "storage.txt")
    
    def run(self):
        raise NotImplementedError
