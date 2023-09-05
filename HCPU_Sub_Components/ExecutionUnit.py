import asyncio
import sys
import os
import time
import numpy as np

class ExecutionUnit:
    def __init__(self, name):
        self.name = name+"-ExecutionUnit"
    
    #def run(self, logger):
    def run(self, logger, instruction, program, memory):
        logger.info(f"@{self.name}.run")
        
        # 1s delay
        time.sleep(1)
        
        logger.info(f"@{self.name}.run: Done")