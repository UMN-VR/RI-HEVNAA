#BusManager.py
import asyncio
import sys
import os
import time
import numpy as np
import logging

class BusManager:
    def __init__(self):
        print("@BusManager.init:")
        self.execute_enabled = True 

    async def execute(self):
        print("@BusManager.execute: Start")

        #Create logger
        logger = logging.getLogger('BusManager')
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('logs/BusManager.log')
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
        print("@BusManager.execute: Done")
    

    async def run(self,logger):
        logger.info("@BusManager.run: Start")

        #wait 5s
        time.sleep(5)

        logger.info("@BusManager.run: Done")