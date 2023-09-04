import asyncio
import sys
import os
import time
import numpy as np

class ControlUnit:
    def __init__(self, name):
        self.name = name+"-ControlUnit"

    def run(self):
        print(f"@{self.name}.run_control_unit: Running Control Unit")
        print(f"@{self.name}.run_control_unit: Done")