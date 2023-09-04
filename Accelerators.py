import asyncio
import sys
import os
import time
import numpy as np

class Accelerators:
    def __init__(self):
        print("@Accelerators.init: Initializing Accelerators")

        self.execute_enabled = True

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
        print(f"@Accelerators.execute: Starting Execution")

        #if accelerators is not empty
        if self.accelerators:
            print(f"@Accelerators.execute: Accelerators Loaded & not empty")
            #while execute is enabled   
            while(self.execute_enabled):
                #execute each accelerator
                for accelerator in self.accelerators:
                    print(f"@Accelerators.execute: Executing {accelerator.name}")
                    accelerator.execute()

        print(f"@Accelerators.execute: Done")