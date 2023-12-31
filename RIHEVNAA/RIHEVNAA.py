#RIHEVNAA.py
import asyncio
import sys
import os
import time
import numpy as np


from RIHEVNAA.BusManager import BusManager
from RIHEVNAA.WebMonitoringProcess import WebMonitoringProcess
from RIHEVNAA.Accelerators import Accelerators

from RIHEVNAA.Unit import Unit
import logging
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
import traceback


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
        print("\n@RIHEVNAA.init:\n")

        # Initialize components

        # Initialize Bus Manager, which will handle all communication between components
        # Interhemispheric, Agent & other bus communication will be handled by the Bus Manager
        self.bus_manager = BusManager()
        self.web_monitoring_process = WebMonitoringProcess()
        self.accelerators = Accelerators()
        print("@RIHEVNAA.init: DONE: Init Components")
        
        # Initialize Interhemispheric Units
        print("Initializing Interhemispheric Units")

        # Initialize Agent Hemisphere Unit
        self.agent_unit = Unit("A_HCPU", self.bus_manager, self.accelerators)

        # Initialize Right Hemisphere Unit
        self.right_unit = Unit("R_HCPU", self.bus_manager, self.accelerators)

        # Initialize Left Hemisphere Unit
        self.left_unit = Unit("L_HCPU", self.bus_manager, self.accelerators)
    
    


    # Start RI-HEVNAA execution, this will start all components and create 3 separate threads for each hemisphere
    async def execute(self):

        startup_success = True
        print("\n@RIHEVNAA.execute: Starting RI-HEVNAA Execution\n")
        # Create processes
        processes = []
        process_names = ["bus_manager", "web_monitoring_process", "accelerators", "agent_unit", "right_unit", "left_unit"]
        process_coroutines = [self.bus_manager.execute, self.web_monitoring_process.execute, self.accelerators.execute, self.agent_unit.execute, self.right_unit.execute, self.left_unit.execute]

        for name, coroutine in zip(process_names, process_coroutines):
            try:
                print(f"Creating process for {name}")
                p = Process(target=run_coroutine_in_new_process, args=(coroutine,))
                p.name = name
                processes.append(p)
            except Exception as e:
                startup_success = False
                print(f"Failed to create process for {name}: {e}")

        # Start processes
        for p in processes:
            try:
                print(f"Attempting to start process {p.name}")
                p.start()
                print(f"pid: {p.pid}, daemon: {p.daemon}, alive: {p.is_alive()}, exitcode: {p.exitcode}")
            except Exception as e:
                startup_success = False
                print(f"Failed to start process {p.name}: {e} {e.with_traceback}")
                traceback.print_tb(e.__traceback__)
                print(f"Cause: {e.__cause__}")
                print(f"Context: {e.__context__}")
                print(f"Type: {e.__class__}")
                print(f"Args: {e.args}")
                print(f"Doc: {e.__doc__}")

        if not startup_success:
            print("@RIHEVNAA.execute: ⚠️WARNING⚠️ Failed to start all processes, exiting")
            return
        elif startup_success:
            print("\n@RIHEVNAA.execute: All processes started successfully, starting execution\n")

        # Wait for processes to finish
        for p in processes:
            p.join()

        print("@RIHEVNAA.execute: Done")

