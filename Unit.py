import asyncio
import sys
import os
import time
import numpy as np
from HCPU import HCPU
from Accelerators import Accelerators


class Unit:
    def __init__(self, name, bus_manager, accelerators):
        print(f"@Unit.init: Starting {name}")
        self.name = name

        # link accelerators from Accelerators.py
        self.accelerators = accelerators.link_accelerators(self.name)

        # Initialize Hemisphere Central Processing Unit
        self.unit_HCPU = HCPU(self.name, self.accelerators, bus_manager)

    async def execute(self):
        print(f"@{self.name}_Unit.execute")

        # Execute Agent Central Processing Unit
        await self.unit_HCPU.execute()

        print("@R_Unit.execute: Done")
