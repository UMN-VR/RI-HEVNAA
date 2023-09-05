import asyncio
import sys
import os
import time
import numpy as np

class MemoryUnit:
    def __init__(self, name):
        self.name = name+"-MemoryUnit"
    
    #async def run(self, logger):
    async def run(self, logger, RAM, instruction, program, memory, result):
        logger.info(f"@{self.name}.run")
        
        # 1s delay
        time.sleep(1)
        
        logger.info(f"@{self.name}.run: Done")
        return RAM