# This file takes as inputs 2 strings, the first 'string' with the string to be printed and a second one 'retry' with the number of times the string should be printed. The output is a string with the string repeated 'repeat' times, or if 'yes' is repeated infinitely. 
import sys
import os
import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("string", help="String to be printed")
parser.add_argument("repeat", help="Number of times the string should be printed")
args = parser.parse_args()

def print_string():
    if args.repeat == "yes":

        while True:
            print(args.string)

    else:
        if args.repeat == "0":
            return "DONE"
        
        print(args.string)
        num = int(args.repeat)
        string = str(num-1)
        return string

print_string()

