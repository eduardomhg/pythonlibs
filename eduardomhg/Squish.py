#!/usr/bin/python

##### TEMPLATE USAGE: REMOVE ALL THE LINES STARTING WITH #### (INFORMATIVE) AFTER READING THEM.

##### The string below is a 'doc string', used as a comment but is also used to auto-document the code.
##### They can be shown using [script].__doc__ and help(script).

"""

Contains functions related to the Build of firmware applications and external tools.

This module is not a script. It must be imported from other modules or scripts.

This script has been tested with Python 3.4 (https://www.python.org/)

"""

import eduardomhg.CommandLine
import eduardomhg.EnvironmentVariables
import os
import os.path
import shutil
import distutils.dir_util

SQUISH_DIR = os.path.join(eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("SQUISH_PATH"), "bin")

def ConfigureServer(attachableAUT, autIP="127.0.0.1", autPort=2222):
    """This function..."""
    return eduardomhg.CommandLine.Execute(os.path.join(SQUISH_DIR, "squishserver") + " --config addAttachableAUT " +
                                   attachableAUT + " " + autIP + ":" + str(autPort))

def ConfigureGlobalScriptsDir(path):
    return eduardomhg.EnvironmentVariables.WriteEnvironmentVariable("SQUISH_SCRIPT_DIR", path)

def StartServer(port=1111):
    """This function..."""
    return eduardomhg.CommandLine.Execute(os.path.join(SQUISH_DIR, "squishserver") + " --port=" + str(port))

def StopServer(port=1111):
    """This function..."""
    return eduardomhg.CommandLine.Execute(os.path.join(SQUISH_DIR, "squishserver") + " --port=" + str(port) + " --stop")    

def BuildStartServerCommand(port=1111):
    """This function..."""
    return [os.path.join(SQUISH_DIR, "squishserver"), "--port=" + str(port)]

def StartAttachedAUT(command, autPort=2222):
    """This function..."""
    return eduardomhg.CommandLine.Execute(os.path.join(SQUISH_DIR, "startaut") + " --port=" + str(autPort) +
                                   " " + command)

def BuildAttachedAUTCommand(command, autPort=2222):
    """This function..."""
    if isinstance(command, list):
        return [os.path.join(SQUISH_DIR, "startaut"), "--port=" + str(autPort)] + command
    else:
        return [os.path.join(SQUISH_DIR, "startaut"), "--port=" + str(autPort)] + command.split()

def RunTestSuite(suiteDir, resultsDir, serverPort=1111):
    """This function..."""
    return eduardomhg.CommandLine.Execute(os.path.join(SQUISH_DIR, "squishrunner") + " --port=" + str(serverPort) +
                                   " --testsuite " + suiteDir + " --exitCodeOnFail 1 --reportgen html," + 
                                   os.path.realpath(resultsDir))
    
def RunTestSuites(suitesDir, suiteNames, resultsDir, exitOnFirstFail=False, serverPort=1111):
    """This function..."""
    exitCode = 0

    for suite in suiteNames:
        code = RunTestSuite(os.path.join(suitesDir, suite), os.path.join(resultsDir, suite), serverPort)
        if code != 0:
            if exitOnFirstFail:
                exitCode = code
                break
            else:
                exitCode = exitCode + code

    return exitCode

def MergeSquishHTMLReports(baseResultsDir, mergedResultsDir):
    """This function..."""

    mergedResultsJSPath = os.path.join(mergedResultsDir, "data", "results-v1.js")

    # Create list with suite folder names.
    suites = os.listdir(baseResultsDir)
    suites.sort()

    # Create ouput directory.
    if (os.path.exists(mergedResultsDir)):
        shutil.rmtree(mergedResultsDir)
    os.makedirs(mergedResultsDir)

    # Copy all files and folders from the first test suite.
    for folder in os.listdir(baseResultsDir):
        if folder.startswith("suite_"):
            distutils.dir_util.copy_tree(os.path.join(baseResultsDir, folder), mergedResultsDir)
            break

    # Delete the data/dataresults-v1.js        
    os.remove(mergedResultsJSPath)

    # Copy all data/dataresults-v1.js from each suite and remove the first line of each one, but the first one
    n = 0
    for suite in suites:    
        sourcePath = os.path.join(baseResultsDir, suite, "data", "results-v1.js")
        destPath = os.path.join(mergedResultsDir, "data", "results-" + suite + "_temp.js")

        shutil.copy2(sourcePath, destPath)        
        
        tempFile = open(destPath, "r")
        finalFile = open(os.path.join(mergedResultsDir, "data", "results-" + suite + ".js"), "w")
        
        for line in tempFile:
            if (line != "var data = [];\n") or (n < 1):
                finalFile.write(line)
        n = n + 1        
        tempFile.close()        
        finalFile.close()    
        
        os.remove(destPath)

    # Modify index.html to added all the copied JS files from each suite.
    indexPath = os.path.join(mergedResultsDir, "index.html")
    tempIndexPath = os.path.join(mergedResultsDir, "index_temp.html")
    os.rename(indexPath, tempIndexPath)        

    tempFile = open(tempIndexPath, "r")
    finalFile = open(indexPath, "w")

    for line in tempFile:
        if (line != '<script type="text/javascript" src="data/results-v1.js"></script>\n'):
            finalFile.write(line)
        else:
            for suite in suites:
                finalFile.write('<script type="text/javascript" src="' + os.path.join("data", "results-" + suite + ".js") + '"></script>\n')       

    tempFile.close()        
    finalFile.close()        
    os.remove(tempIndexPath)

    print("Created merged report in " + mergedResultsDir)

    return 0    

# This only executes if this script has been directly from the command line (not imported from another script).
if __name__ == '__main__':
    eduardomhg.Utilities.PrintInvalidModuleUsage(__doc__)
  