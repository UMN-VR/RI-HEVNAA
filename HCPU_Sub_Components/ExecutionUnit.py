import asyncio
import sys
import os
import time
import numpy as np

class ExecutionUnit:
    def __init__(self, name):
        self.name = name+"-ExecutionUnit"
    
    def run(self):
        print(f"@{self.name}.run_execution_unit: Running Execution Unit")
        # 1s delay
        time.sleep(1)
        
        print(f"@{self.name}.run_execution_unit: Done") 