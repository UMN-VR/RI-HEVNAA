import asyncio
import sys
import os
import time
import numpy as np
from BusManager import BusManager
from WebMonitoringProcess import WebMonitoringProcess
from Unit import Unit
import logging
import multiprocessing
from Accelerators import Accelerators
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process


def setup_logger(process_name):
    logger = logging.getLogger(process_name)
    logger.setLevel(logging.INFO)
    
    fh = logging.FileHandler(f"logs/{process_name}.log")
    fh.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)
    return logger

def run_coroutine_in_new_process(coroutine_func, *args, **kwargs):
    process_name = coroutine_func.__name__
    
    # Clear previous handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Setup logger for this process
    logger = setup_logger(process_name)
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    coroutine = coroutine_func(*args, **kwargs)
    logger.info(f"@run_coroutine_in_new_process: {type(coroutine)}")
    
    if asyncio.iscoroutine(coroutine):
        loop.run_until_complete(coroutine)
    else:
        logger.error(f"Function {coroutine_func.__name__} did not return a coroutine.")
        raise TypeError("Not a coroutine")


class RIHEVNAA:

    def __init__(self):
        print("@RIHEVNAA: Initializing RI-HEVNAA Components")

        # Initialize components

        # Initialize Bus Manager, which will handle all communication between components
        # Interhemispheric, Agent & other bus communication will be handled by the Bus Manager
        self.bus_manager = BusManager()
        self.web_monitoring_process = WebMonitoringProcess()
        self.accelerators = Accelerators()

        # Initialize Accelerators
        self.accelerators.load_accelerators("accelerators")
        
        # Initialize Interhemispheric Units

        # Initialize Agent Hemisphere Unit
        self.agent_unit = Unit("A_HCPU", self.bus_manager, self.accelerators)

        # Initialize Right Hemisphere Unit
        self.right_unit = Unit("R_HCPU", self.bus_manager, self.accelerators)

        # Initialize Left Hemisphere Unit
        self.left_unit = Unit("L_HCPU", self.bus_manager, self.accelerators)
    
    


    # Start RI-HEVNAA execution, this will start all components and create 3 separate threads for each hemisphere
    async def execute(self):
        print("@RIHEVNAA.execute: Starting RI-HEVNAA Execution")

        # Create processes

        processes = []
        processes.append(Process(target=run_coroutine_in_new_process, args=(self.bus_manager.execute,)))
        processes.append(Process(target=run_coroutine_in_new_process, args=(self.web_monitoring_process.execute,)))
        processes.append(Process(target=run_coroutine_in_new_process, args=(self.accelerators.execute,)))
        processes.append(Process(target=run_coroutine_in_new_process, args=(self.agent_unit.execute,)))
        processes.append(Process(target=run_coroutine_in_new_process, args=(self.right_unit.execute,)))
        processes.append(Process(target=run_coroutine_in_new_process, args=(self.left_unit.execute,)))

        # Start processes
        for p in processes:
            p.start()
            print(f"@RIHEVNAA.execute: Starting process {p.name}, pid: {p.pid}, daemon: {p.daemon}, alive: {p.is_alive()}, exitcode: {p.exitcode}")
        
        # Wait for processes to finish
        for p in processes:
            p.join()


        print("@RIHEVNAA.execute: Done")
