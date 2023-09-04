# Main file for RI-HEVNAA Architecture

import asyncio
import sys
import os
import time
import numpy as np
from RIHEVNAA import RIHEVNAA

# Main function
async def main():
    print("@main: Starting RI-HEVNAA System")

    ri_hevnaa = RIHEVNAA()
    
    await ri_hevnaa.execute()

    print("@main: Stopping RI-HEVNAA System")

#If File is main.py run main
if __name__ == "__main__":
    asyncio.run(main())