import os
import sys

class State:
    def __init__(self, state_machine):
        # Determine the base path for resources
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        sys.path.append(base_path)
        
        self.state_machine = state_machine
        self.banner_path = os.path.join(base_path, "resources", "banner.txt")
        self.storage_path = os.path.join(base_path, "resources", "storage.txt")
    
    def run(self):
        raise NotImplementedError
