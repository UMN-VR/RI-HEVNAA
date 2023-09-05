import asyncio
import sys
import os
import time
import numpy as np

class ExecutionUnit:
    def __init__(self, name):
        self.name = name+"-ExecutionUnit"
    
    #async def run(self, logger):
    async def run(self, logger, instruction, program, memory):
        logger.info(f"@{self.name}.run")

        #Init return values
        result = None
        
        # 1s delay
        time.sleep(1)
        
        logger.info(f"@{self.name}.run: Done")
        return result