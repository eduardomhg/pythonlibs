#!/usr/bin/python

"""

Contains functions for command-line invocation (initially intended for build scripts).

This module is not a script. It must be imported from other modules or scripts.

This module has been tested with Python 3.4 (https://www.python.org/)

"""

import subprocess
import sys
import os
from eduardomhg.Trace import Trace, ForeColor

def Execute(command, cwd=""):
    """Executes a command in the current directory.
    
    Args:
    command: str, the command to execute.
    
    Returns: the exit code of the executed command.
    """
        
    Trace("Executing '" + command + "'...", ForeColor.CYAN)
    
    if cwd != "":
        savedWD = os.getcwd()
        os.chdir(cwd)
    
    code = subprocess.call(command, shell=True)

    if cwd != "":
        os.chdir(savedWD)


    if code == 0:
        Trace("Exit code: " + str(code), ForeColor.GREEN)
    else:
        Trace("Exit code: " + str(code), ForeColor.RED)
    
    return code

def ExecuteSequence(commands):
    """Executes a sequence of commands in the current directory. If one of the command fails (returns an exit code
    greater than 0), then the sequence is aborted and the exit code is returned.
    
    Args:
    command: list<str>, the commands to execute.
    
    Returns: the exit code of the last executed command.
    """
    exitCode = 0
    for command in commands:
        exitCode = Execute(command)
        if exitCode != 0:
            break
    return exitCode

def ExecuteAndWait(command):
    """Executes a command in the current directory and waits for it to terminate.
    It is equivalent to MSDOS "start /w"
    
    Args:
    command: str, the command to execute.
    
    Returns: the exit code of the executed command.
    """
    print "Executing '" + command + "' and waiting for it to finish..."
    print
    sys.stdout.flush()
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    return process.returncode    
    
# This only executes if this script has been directly from the command line (not imported from another script).
if __name__ == '__main__':
    eduardomhg.Utilities.PrintInvalidModuleUsage(__doc__)