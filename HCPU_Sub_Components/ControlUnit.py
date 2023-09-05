import asyncio
import sys
import os
import time
import numpy as np
import logging
from multiprocessing import Queue
import json


# define the states of the A-CPU
STATE_IDLE = 'idle'
STATE_RUNNING = 'running'
STATE_HALTED = 'halted'

class ControlUnit:

    def load_pathway(self, pathway):
        # Add a pathway to the A-CPU's pathway dictionary
        # The pathway's ID is used as the key

        #Open the JSON file
        with open(pathway, 'r') as f:
            #Load the JSON file as a dictionary
            pathway = json.load(f)

        self.pathways.append(pathway)


    def load_pathways(self, folder):
        #A pathway is saved as a JSON file  
        #Load all JSON files in the folder
        pathways = []
        
        # Get all subfolders in the folder
        subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
        # for each subfolder in the folder
        for subfolder in subfolders:
            # Get all files in the subfolder
            files = [f.path for f in os.scandir(subfolder) if f.is_file()]
            # for each file in the subfolder
            for file in files:
                # if the file is a JSON file
                if file.endswith(".json"):

                    #if file is 'pathway.json' 
                    if file == "pathway.json":
                        # load the pathway
                        self.load_pathway(file)
                        print(f"Loaded pathway: {file}")
                    
                    else: 
                        # load the sub-pathway
                        self.load_pathway(file)
                        print(f"Loaded sub-pathway: {file}")
                    
        

    def __init__(self, name, bus_manager):
        self.name = name+"-ControlUnit"
        self.bus_manager = bus_manager
        self.state = STATE_IDLE
        self.task_queue = Queue()
        self.pathways = []
        self.load_pathways("pathways")
    

    #async def run(self, logger):
    async def run(self, logger, RAM, Accelerators):
        logger.info(f"@{self.name}.run")

        #Init return values
        instruction = None
        program = None
        memory = None



        #Check the Task Queue for new tasks
        if self.task_queue.empty():
            # 1s delay
            time.sleep(1)
        else:
            logger.info(f"New task found")


        
        
        logger.info(f"@{self.name}.run: Done")
        return instruction, program, memory