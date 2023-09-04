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

# def run_coroutine(coroutine):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     return loop.run_until_complete(coroutine)

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



# def run_coroutine_in_new_process(coroutine_func, *args, **kwargs):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     coroutine = coroutine_func(*args, **kwargs)
#     print(f"@run_coroutine_in_new_process: {type(coroutine)}")
#     coroutine = coroutine_func(*args, **kwargs)
#     if asyncio.iscoroutine(coroutine):
#         loop.run_until_complete(coroutine)
#     else:
#         raise TypeError("Not a coroutine")


# def run_coroutine_in_new_process(coroutine):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(coroutine())

# def run_in_new_process(target, *args):
#     p = Process(target=target, args=args)
#     p.start()
#     return p


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

        # Initialize Agent Unit
        self.agent_unit = Unit("A_CPU", self.bus_manager, self.accelerators)

        # Initialize Right Hemisphere Unit
        self.right_unit = Unit("R_CPU", self.bus_manager, self.accelerators)

        # Initialize Left Hemisphere Unit
        self.left_unit = Unit("L_CPU", self.bus_manager, self.accelerators)
    
    


    # Start RI-HEVNAA execution, this will start all components and create 3 separate threads for each hemisphere
    async def execute(self):
        print("@RIHEVNAA.execute: Starting RI-HEVNAA Execution")

        # t1 = multiprocessing.Process(target=self.web_monitoring_process.execute)
        # t2 = multiprocessing.Process(target=self.bus_manager.execute)
        # t3 = multiprocessing.Process(target=self.accelerators.execute)
        # t4 = multiprocessing.Process(target=self.agent_unit.execute)
        # t5 = multiprocessing.Process(target=self.right_unit.execute)
        # t6 = multiprocessing.Process(target=self.left_unit.execute)

        # # Start threads
        # t1.start(), t2.start(), t3.start(), t4.start(), t5.start(), t6.start()

        # # Wait for threads to finish
        # t1.join(), t2.join(), t3.join(), t4.join(), t5.join(), t6.join()


        # with ThreadPoolExecutor(max_workers=6) as executor:
        #     executor.submit(run_coroutine(self.web_monitoring_process.execute)),
        #     executor.submit(run_coroutine(self.bus_manager.execute)),
        #     executor.submit(run_coroutine(self.accelerators.execute)),
        #     executor.submit(run_coroutine(self.agent_unit.execute)),
        #     executor.submit(run_coroutine(self.right_unit.execute)),
        #     executor.submit(run_coroutine(self.left_unit.execute))

        # await asyncio.gather(
        #     self.bus_manager.execute(),
        #     self.web_monitoring_process.execute(),
        #     self.accelerators.execute(),
        #     self.agent_unit.execute(),
        #     self.right_unit.execute(),
        #     self.left_unit.execute()
        # )

        # run_in_new_process(self.web_monitoring_process.execute)
        # run_in_new_process(self.bus_manager.execute)
        # run_in_new_process(self.accelerators.execute)

        # run_in_new_process(self.agent_unit.execute)
        # run_in_new_process(self.right_unit.execute)
        # run_in_new_process(self.left_unit.execute)

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
        
        # Wait for processes to finish
        for p in processes:
            p.join()


        print("@RIHEVNAA.execute: Done")
