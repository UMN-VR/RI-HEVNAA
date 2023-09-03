import asyncio
import sys
import os
import time
import numpy as np

class ControlUnit:
    def __init__(self, name):
        self.name = name+"-ControlUnit"