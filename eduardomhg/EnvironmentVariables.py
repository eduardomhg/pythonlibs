#!/usr/bin/python

"""

Contains functions for reading, writing and creating environment variables.

This module is not a script. It must be imported from other modules or scripts.

This module has been tested with Python 3.4 (https://www.python.org/)

"""

import os
import Utilities

def CheckEnvironmentVariableExists(variableName):
    """Checks if an environment variable exists.
    
    Args:
    variableName: str, the name of the environment variable.
    
    Returns: bool, whether the variable exists or not.
    """
    return (os.getenv(variableName) != None)

def ReadEnvironmentVariable(variableName):
    """Reads the value of an environment variable, if it exists. Otherwise raises a ValueError.
    
    Args:
    variableName: str, the name of the environment variable.
    
    Returns: str, the variable value.
    
    Raises: 
    ValueError, if the variable does not exist.
    """
    #value = os.getenv(variableName)
    #if value == None:
    #    raise ValueError("The variable does not exist")
    if variableName in os.environ:
        return os.environ[variableName]
    else:
        return ""
    
def CreateEnvironmentVariable(variableName, variableValue):
    """Creates environment an variable, if it does not exist. Otherwise raises a ValueError.
    
    Args:
    variableName: str, the name of the environment variable.
    variableValue: str, the value to be assigned to the created environment variable.
    
    Raises: 
    ValueError, if the variable already exists.
    """
    if os.name == 'nt':
        if not CheckEnvironmentVariableExists(variableName):
            code = os.system("SETX -m " + variableName + " " + variableValue)
            if code != 0:
                raise Exception("Error executing SETX: " + str(code))
        else:
            raise ValueError("The variable already exists")
    else:
        if not CheckEnvironmentVariableExists(variableName):
            os.putenv(variableName, variableValue)
        else:
            raise ValueError("The variable already exists")

def WriteEnvironmentVariable(variableName, variableValue):
    """Writes the environment variable. If it does not exist, it is created.
    
    Args:
    variableName: str, the name of the environment variable.
    variableValue: str, the value to be assigned to the variable.
    """
    os.environ[variableName] = variableValue
    
def AppendToEnvironmentVariable(variableName, value):
    """Appends a value to the environment variable. If it does not exist, it is created.
    
    Args:
    variableName: str, the name of the environment variable.
    value: str, the value to be append to the current variable value.
    """
    if not CheckEnvironmentVariableExists(variableName):
        CreateEnvironmentVariable(variableName, value)
    else:
        currentValue = ReadEnvironmentVariable(variableName)
        WriteEnvironmentVariable(variableName, currentValue + value)

# This only executes if this script has been directly from the command line (not imported from another script).
if __name__ == '__main__':
    Utilities.PrintInvalidModuleUsage(__doc__)
