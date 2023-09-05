import asyncio
import sys
import os
import time
import numpy as np
import logging
from queue import Queue, Empty
import threading

# define the states of the A-CPU
STATE_IDLE = 'idle'
STATE_RUNNING = 'running'
STATE_HALTED = 'halted'

class ControlUnit:
    def __init__(self, name, bus_manager):
        self.name = name+"-ControlUnit"
        self.bus_manager = bus_manager
        self.state = STATE_IDLE
        self.task_queue = Queue()
        self.pathways = {}
    
    def load_pathway(self, pathway):
        # Add a pathway to the A-CPU's pathway dictionary
        # The pathway's ID is used as the key
        self.pathways[pathway.pathway_id] = pathway

    def run(self, logger):
    #def run(self, logger, RAM, Accelerators):
        logger.info(f"@{self.name}.run")

        #Check the Task Queue for new tasks
        if self.task_queue.empty():
            # 1s delay
            time.sleep(1)
        else:
            logger.info(f"New task found")


        
        
        logger.info(f"@{self.name}.run: Done")