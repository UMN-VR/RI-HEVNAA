import asyncio
import sys
import os
import time
import numpy as np

# Hemisphere Central Processing Unit, a Von Neumann Architecture inspired program that acts like a high level CPU. Takes in 'name' argument
class HCPU:
    def __init__(self, name, accelerators, bus_manager):
        print(f"@A_CPU.init: Start {name}")
        # Initialize components

        self.execute_enabled = True
        self.name = name

        # Init Memory Unit
        self.memory_unit = MemoryUnit(self.name)

        # Init Control Unit
        self.control_unit = ControlUnit(self.name)
        
        # Init Control Unit
        self.execution_unit = ExecutionUnit(self.name)

        # Init Accelerators
        self.accelerators = accelerators

        print(f"@A_CPU.init: {name} Done")
    
    async def execute(self):
        print("@A_CPU.execute: Start")
        while(self.execute_enabled):
            self.run()
        print("@A_CPU.execute: Done")
    
    async def run(self):

        print(f"@A_CPU.run: {self.name} Running")

        # Run Accelerators
        self.accelerators.run_accelerators()

        # Run Control Unit
        self.control_unit.run_control_unit()

        # Run Execution Unit
        self.execution_unit.run_execution_unit()

        print(f"@A_CPU.run: {self.name} Done")