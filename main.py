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

    delete_logs = True

    if delete_logs:
        # Delete all logs
        print("@main: Deleting logs")
        for file in os.listdir("logs"):
            os.remove(f"logs/{file}")
    
    # make sure logs folder exists
    if not os.path.exists("logs"):
        os.makedirs("logs")
    

    # Init RI-HEVNAA

    ri_hevnaa = RIHEVNAA()

    await ri_hevnaa.execute()

    print("@main: Stopping RI-HEVNAA System")

#If File is main.py run main
if __name__ == "__main__":
    asyncio.run(main())