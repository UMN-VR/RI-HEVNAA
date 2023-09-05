import asyncio
import sys
import os
import time
import numpy as np
import logging

class HCPU:
    def __init__(self, name,  accelerators, bus_manager):
        print("@HCPU: Initializing Web Monitoring Process")
        self.execute_enabled = True 

    async def execute(self):
        print("@HCPU.execute: Start")

        #Create logger
        logger = logging.getLogger('HCPU')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('logs/HCPU.log')
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

        while(self.execute_enabled):
            await self.run(logger)
        print("@HCPU.execute: Done")
    

    async def run(self, logger):
        #print("@HCPU.run: Start")
        logger.info("@HCPU.run:")

        #wait 11s
        time.sleep(11)

        #print("@HCPU.run: Done")
        logger.info("@HCPU.run: Done")
