import asyncio
import sys
import os
import time
import numpy as np

class WebMonitoringProcess:
    def __init__(self):
        print("@WebMonitoringProcess: Initializing Web Monitoring Process")
        self.execute_enabled = True 

    async def execute(self):
        print("@WebMonitoringProcess.execute: Start")
        while(self.execute_enabled):
            await self.run()
        print("@WebMonitoringProcess.execute: Done")
    

    async def run(self):
        print("@WebMonitoringProcess.run: Start")

        #wait 11s
        time.sleep(11)

        print("@WebMonitoringProcess.run: Done")
