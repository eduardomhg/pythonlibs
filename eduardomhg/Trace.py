#!/usr/bin/python

"""

Contains functions for logging and tracing messages from some other script.

This module is not a script. It must be imported from other modules or scripts.

This module has been tested with Python 3.4 (https://www.python.org/)

"""

from eduardomhg.Utilities import CheckedImport, PrintInvalidModuleUsage

colorama = CheckedImport("colorama")

ForeColor = colorama.Fore

# Initialize colorama
colorama.init(autoreset=True, strip=False)

# Trace generic function
def Trace(message, color=None):
    if color == None:
        print(message)
    else:
        print(color + message)

# Trace specific functions

def TraceError(message):
    Trace(message, ForeColor.RED)

def TraceSuccess(message):
    Trace(message, ForeColor.GREEN)

def TraceWarning(message):
    Trace(message, ForeColor.YELLOW)

def TraceInfo(message):
    Trace(message, ForeColor.CYAN)   

# This only executes if this script has been directly from the command line (not imported from another script).
if __name__ == '__main__':
    PrintInvalidModuleUsage(__doc__)
