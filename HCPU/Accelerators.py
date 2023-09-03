import asyncio
import sys
import os
import time
import numpy as np

class Accelerators:
    def __init__(self, name):
        self.name = name+"-Accelerators"

    def load_accelerators(self, folder_path):
        # load JSON files with accelerator information in A_CPU/accelerators folder
        accelerator_info = {}
        return accelerator_info
    
    def init_accelerators(self):
        print(f"@{self.name}.init_accelerators: Initializing Accelerators")
        self.accelerators = []
        print(f"@{self.name}.init_accelerators: Done")
    
    def run_accelerators(self):
        print(f"@{self.name}.run_accelerators: Running Accelerators")
        print(f"@{self.name}.run_accelerators: Done")