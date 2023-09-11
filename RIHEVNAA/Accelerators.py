import asyncio
import sys
import os
import time
import numpy as np
import logging

class Accelerators:
    def __init__(self):
        print("@Accelerators.init:")

        self.execute_enabled = True


    def init_logger(self):
        #Create logger
        logger = logging.getLogger(f'Accelerators')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(f'logs/Accelerators.log')
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

    def load_accelerators(self, folder_path):
        # load JSON files with accelerator information in A_CPU/accelerators folder

        #Accelerator objects
        self.accelerators = []

        #info for each accelerator
        accelerator_info = {}
        return accelerator_info
    
    def link_accelerators(self, name):
        print(f"@{name}.link_accelerators:")

        # link accelerators to unit

    
        self.accelerators = []
        return self.accelerators

    
    async def execute(self):
        print("@Accelerators.execute: Start")

        self.init_logger()

        self.logger.info(f"@Accelerators.execute: Starting Execution")
        

        self.load_accelerators("accelerators")

        while(self.execute_enabled):
                if self.accelerators:
                    #execute each accelerator
                    for accelerator in self.accelerators:
                        print(f"@Accelerators.execute: Executing {accelerator.name}")
                        accelerator.execute()
                else:
                    # 1s delay
                    time.sleep(1)
                   
                    self.logger.info(f"@Accelerators.execute: No accelerators to execute")

        self.logger.info(f"@Accelerators.execute: Done")  
