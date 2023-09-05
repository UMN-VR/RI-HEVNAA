#HCPU.py
import asyncio
import sys
import os
import time
import numpy as np
from HCPU_Sub_Components.MemoryUnit import MemoryUnit
from HCPU_Sub_Components.ControlUnit import ControlUnit
from HCPU_Sub_Components.ExecutionUnit import ExecutionUnit
import logging


# Hemisphere Central Processing Unit, a Von Neumann Architecture inspired program that acts like a high level CPU. Takes in 'name' argument
class HCPU:
    def __init__(self, name, accelerators, bus_manager):
        print(f"@{name}.init:")


        # Initialize components

        self.execute_enabled = True
        self.name = name

        # Init Memory Unit
        self.memory_unit = MemoryUnit(self.name)

        # Init Control Unit
        self.control_unit = ControlUnit(self.name, bus_manager)
        
        # Init Control Unit
        self.execution_unit = ExecutionUnit(self.name)

        # Init Accelerators
        self.accelerators = accelerators

        print(f"@{self.name}.init_logger:")
        #Create logger
        self.logger = logging.getLogger(f'{self.name}')
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(f'logs/{self.name}.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        print(f"@{self.name}.init: Done")

    
    async def execute(self):
        print(f"@{self.name}.execute:")

        self.logger.info(f"@{self.name}.execute:")

        while(self.execute_enabled):
            await self.run(self.logger)
       
        self.logger.info(f"@{self.name}.execute: Done")
    
    async def run(self):

        #print(f"@A_CPU.run: {self.name} Running")
        self.logger.info(f"@{self.name}.run:")

        # # Run Control Unit
        # instruction, program, memory = await self.control_unit.run(logger, self.RAM, self.accelerators)

        # # Run Execution Unit
        # result = await self.execution_unit.run(logger, instruction, program, memory)

        # # Run Memory Unit
        # self.RAM = await self.memory_unit.run(logger, program, memory, result)

        # Run Control Unit
        self.control_unit.run(self.logger)

        # Run Execution Unit
        self.execution_unit.run(self.logger)

        # Run Memory Unit
        self.memory_unit.run(self.logger)

        #print(f"@A_CPU.run: {self.name} Done")
        self.logger.info(f"@{self.name}.run: Done")

