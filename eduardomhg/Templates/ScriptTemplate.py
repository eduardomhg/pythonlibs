#!/usr/bin/python

##### TEMPLATE USAGE: REMOVE ALL THE LINES STARTING WITH #### (INFORMATIVE) AFTER READING THEM.

##### The string below is a 'doc string', used as a comment but is also used to auto-document the code.
##### They can be shown using [script].__doc__ and help(script).

"""

(General description of what the script does)

The goal of this script is...

Example of script invocation: 

    python ScriptTemplate.py

This script has been tested with Python 3.4 (https://www.python.org/)

"""

##### import module1
##### import module2 # This module is necessary for...
##### import thirdpartymodule2 # Download URL: thirdparty.python.org
import sys

##### Constants (strings, numbers, etc) used in the script should be defined here.

##### A_CONSTANT = 1
##### SOME_CONSTANT_STRINGS = [
#####     "string 1",
#####     "string 2"]

##### Code should be written here INSIDE functions (not at script level).
##### A doc string (at the beginning) must document its purpose and usage of each function.

##### def Function():
#####    """This function..."""
#####    (Function code)

##### Entry point, only if this module may be used as a standalone script (called directly from the command line).
##### Delete for libraries.
def main():
    # If required, command-line arguments should normally parsed here.

    print
    print "This is the official firmware template for python scripts."
    print "Auto-generated documentation:"
    print __doc__

    # It is mandatory to explicitly return an exit code (0 for success).
    sys.exit(0)

# This only executes if this script has been directly from the command line (not imported from another script).
if __name__ == '__main__':
  main()