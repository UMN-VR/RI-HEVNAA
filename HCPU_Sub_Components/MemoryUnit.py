import asyncio
import sys
import os
import time
import numpy as np

class MemoryUnit:
    def __init__(self, name):
        self.name = name+"-MemoryUnit"
    
    def run(self):
        print(f"@{self.name}.run_memory_unit: Running Memory Unit")
        print(f"@{self.name}.run_memory_unit: Done")