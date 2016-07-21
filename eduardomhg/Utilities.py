#!/usr/bin/python

"""

Contains general utility functions.

This module is not a script. It must be imported from other modules or scripts.

This module has been tested with Python 3.4 (https://www.python.org/)

"""

import sys

def PrintInvalidModuleUsage(moduleDoc):
    """ Prints usage information when a non-executable module is invoked from the command-line """
    print
    print "This module cannot be executed as a script. It must be imported from other modules or scripts."
    print
    print "Auto-generated documentation:"
    print moduleDoc
    sys.exit(1)


def CheckedImport(packageName):
    try:
        from importlib import import_module 
        return import_module(packageName)
    except ImportError:
        print("Module " + packageName + " not found. Trying to download it with pip...")
        import pip
        try:
            exitCode = pip.main(["install", packageName])
            if exitCode != 0:
                raise Exception()
        except:
            raise Exception('Unable to install missing module, try to execute the script with sudo!')

    return import_module(packageName)


# This only executes if this script has been directly from the command line (not imported from another script).
if __name__ == '__main__':
    PrintInvalidModuleUsage(__doc__)
