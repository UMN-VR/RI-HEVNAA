import asyncio
import sys
import os
import time
import numpy as np

class RIHEVNAA:

    def __init__(self):
        print("@RIHEVNAA: Initializing RI-HEVNAA Components")

        # Initialize components

        # Initialize Bus Manager, which will handle all communication between components
        # Interhemispheric, Agent & other bus communication will be handled by the Bus Manager
        self.bus_manager = BusManager()
        self.web_monitoring_process = WebMonitoringProcess()


        # Initialize Interhemispheric Units

        # Initialize Agent Unit
        self.agent_unit = Unit("A_CPU", self.bus_manager)

        # Initialize Right Hemisphere Unit
        self.right_unit = Unit("R_CPU", self.bus_manager)

        # Initialize Left Hemisphere Unit
        self.left_unit = Unit("L_CPU", self.bus_manager)

    
    # Start RI-HEVNAA execution, this will start all components and create 3 separate threads for each hemisphere
    async def execute(self):
        print("@RIHEVNAA.execute: Starting RI-HEVNAA Execution")


        # Start Interhemispheric Units
        await asyncio.gather(
            self.agent_unit.execute(),
            self.right_unit.execute(),
            self.left_unit.execute()
        )


        print("@RIHEVNAA.execute: Done")
