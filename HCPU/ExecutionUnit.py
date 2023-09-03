import asyncio
import sys
import os
import time
import numpy as np

class ExecutionUnit:
    def __init__(self, name):
        self.name = name+"-ExecutionUnit"