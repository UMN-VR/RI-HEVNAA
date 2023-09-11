import asyncio
import sys
import os
import time
import numpy as np
import logging

from RIHEVNAA.HCPU.MemoryUnit import MemoryUnit
from RIHEVNAA.HCPU.ControlUnit import ControlUnit
from RIHEVNAA.HCPU.ExecutionUnit import ExecutionUnit

DEBUG_CONTROL_UNIT = True
DEBUG_EXECUTION_UNIT = True
DEBUG_MEMORY_UNIT = True

class HCPU:
    def __init__(self, name,  accelerators, bus_manager):
        self.name = name
        self.execute_enabled = True
        self.i = 0

        self.start_time = time.time()
        self.end_time = time.time()
        self.duration = self.end_time - self.start_time 

        self.RAM = None

        self.accelerators = accelerators

        print(f"@{self.name}.init:")

        #Init Control Unit
        self.control_unit = ControlUnit(self.name, bus_manager)
        print("Init Control Unit DONE")

        #Init Execution Unit
        self.execution_unit = ExecutionUnit(self.name)
        print("Init Execution Unit DONE")

        # Init Memory Unit
        self.memory_unit = MemoryUnit(self.name)
        print("Init Memory Unit DONE")

    def init_logger(self):
        #Create logger
        logger = logging.getLogger(f'{self.name}')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(f'logs/{self.name}.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        self.logger = logger



    async def execute(self):
        print(f"@{self.name}.execute:")

        self.init_logger()
        
        while(self.execute_enabled):

            self.start_time = time.time()
            self.i += 1

            self.logger.info(f"@{self.name}.execute: Starting run #{self.i} at {self.start_time}")


            #Print Debug Info
            self.logger.info(f"ControlUnit state before run: {self.control_unit.state}")


            # Run HCPU
            await self.run()


            self.end_time = time.time()

            self.duration = self.end_time - self.start_time


            self.logger.info(f"@{self.name}.execute: Ending run #{self.i} at {self.end_time}")
            self.logger.info(f"Cycle Duration: {self.duration}")

        print(f"@{self.name}.execute: Done")
    

    async def run(self):
        #print("@HCPU.run: Start")
        self.logger.info(f"@{self.name}.run:")


        # Run Control Unit
        instruction, program, memory = await self.control_unit.run(self.logger, self.RAM, self.accelerators)

        if DEBUG_CONTROL_UNIT:
            self.logger.info(f"Instruction: {instruction}")
            self.logger.info(f"Program: {program}")
            self.logger.info(f"Memory: {memory}")


        # Run Execution Unit
        result = await self.execution_unit.run(self.logger, instruction, program, memory)

        if DEBUG_EXECUTION_UNIT:
            self.logger.info(f"Result: {result}")
        

        # Run Memory Unit
        self.RAM = await self.memory_unit.run(self.logger, self.RAM, instruction, program, memory, result)

        if DEBUG_MEMORY_UNIT:
            self.logger.info(f"RAM: {self.RAM}")

        self.logger.info(f"@{self.name}.run: Done")
