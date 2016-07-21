#!/usr/bin/python

"""

Adds the eduardomhg python package path to the PYTHONPATH environment variable.

It is assumed that this script is executed from the eduardomhg folder, otherwise it will not work.

Example of script invocation: 

    SetupPYTHONPATH.py

This script has been tested with Python 3.4 (https://www.python.org/)

"""

import sys
import os
import os.path
from ThirdParty import admin
import EnvironmentVariables

def main():
    """Main routine for this script.""" 
    
    # Only on Windows
    if os.name == 'nt':
        if not admin.isUserAdmin():
            admin.runAsAdmin()
            sys.exit(1)
    
    (utcFolder, filename) = os.path.split(__file__)
    (rootFolder, filename) = os.path.split(utcFolder) 
    valueToAppend = "; " + rootFolder
    
    print
    
    if EnvironmentVariables.CheckEnvironmentVariableExists("PYTHONPATH"):
        print "PYTHONPATH already exists, appending '" + valueToAppend + "'..."
        EnvironmentVariables.AppendToEnvironmentVariable("PYTHONPATH", valueToAppend)
    else:
        print "PYTHONPATH does not exist, creating it with value '" + rootFolder + "'..."
        EnvironmentVariables.CreateEnvironmentVariable("PYTHONPATH", rootFolder)

    print
    input("Done. Press Enter to exit...")
    
    # It is mandatory to explicitly return an exit code (0 for success).
    sys.exit(0)

# This only executes if this script has been directly from the command line (not imported from another script).
if __name__ == '__main__':
    main()
