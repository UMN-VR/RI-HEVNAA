import asyncio
import sys
import os
import time
import numpy as np

#name would be A_CPU, R_CPU or L_CPU
class Unit:
    def __init__(self, name, bus_manager):
        print(f"@Unit.init: Starting {name}")
        self.name = name

        # load JSON files with accelerator information in {name}/accelerators folder
        self.accelerators = Accelerators(self.name)
        self.accelerators.load_accelerators(f"{self.name}/accelerators")
        self.accelerators.init_accelerators()

        # Initialize Hemisphere Central Processing Unit
        self.unit_HCPU = HCPU(self.name, self.accelerators, bus_manager)

    async def execute(self):
        print(f"@{self.name}_Unit.execute")

        # Execute Agent Central Processing Unit
        await self.unit_HCPU.execute()

        print("@R_Unit.execute: Done")