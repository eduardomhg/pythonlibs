#!/usr/bin/python

##### TEMPLATE USAGE: REMOVE ALL THE LINES STARTING WITH #### (INFORMATIVE) AFTER READING THEM.

##### The string below is a 'doc string', used as a comment but is also used to auto-document the code.
##### They can be shown using [script].__doc__ and help(script).

"""

Contains functions related to the Build of firmware applications and external tools.

This module is not a script. It must be imported from other modules or scripts.

This script has been tested with Python 3.4 (https://www.python.org/)

"""

##### import module1
##### import module2 # This module is necessary for...
##### import thirdpartymodule2 # Download URL: thirdparty.python.org
import eduardomhg.CommandLine
import eduardomhg.EnvironmentVariables
import os.path
import shutil

### MULTI ###

MULTI5_DIR = eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("MULTI506_PATH")
MULTI6_DIR = eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("MULTI614_PATH")

def _GBuildMULTIProject(multiDir, topProjectFilePath, projectFilePath, options, injectPrefix):
    """This function..."""
    return eduardomhg.CommandLine.Execute(injectPrefix + os.path.join(multiDir, "gbuild") + " " + options + \
                                   " -top " + topProjectFilePath + " " + projectFilePath)

def CleanMULTI5Project(topProjectFilePath, options = "", projectFilePath = "", injectPrefix = ""):
    """This function..."""
    return _GBuildMULTIProject(MULTI5_DIR, topProjectFilePath, projectFilePath, options + " -clean", injectPrefix)

def CleanMULTI6Project(topProjectFilePath, options = "", projectFilePath = "", injectPrefix = ""):
    """This function..."""
    return _GBuildMULTIProject(MULTI6_DIR, topProjectFilePath, projectFilePath, options + " -clean", injectPrefix)
    
def BuildMULTI5Project(topProjectFilePath, options = "", projectFilePath = "", injectPrefix = ""):
    """This function..."""
    return _GBuildMULTIProject(MULTI5_DIR, topProjectFilePath, projectFilePath, options, injectPrefix)

def BuildMULTI6Project(topProjectFilePath, options = "", projectFilePath = "", injectPrefix = ""):
    """This function..."""
    return _GBuildMULTIProject(MULTI6_DIR, topProjectFilePath, projectFilePath, options, injectPrefix)
    
def RebuildMULTI5Project(topProjectFilePath, options = "", projectFilePath = "", injectPrefix = ""):
    """This function..."""
    return _GBuildMULTIProject(MULTI5_DIR, topProjectFilePath, projectFilePath, options + " -cleanfirst", injectPrefix)

def RebuildMULTI6Project(topProjectFilePath, options = "", projectFilePath = "", injectPrefix = ""):
    """This function..."""
    return _GBuildMULTIProject(MULTI6_DIR, topProjectFilePath, projectFilePath, options + " -cleanfirst", injectPrefix)

### CODE COMPOSER ###    

CCS61_DIR = eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("CCS61_PATH")

def _InvokeCCS61(workspacePath, application, arguments, injectPrefix):
    """This function..."""
    """ See http://processors.wiki.ti.com/index.php/Projects_-_Command_Line_Build/Create """
    return eduardomhg.CommandLine.Execute(injectPrefix + os.path.join(CCS61_DIR, "eclipsec") + " -noSplash -data " + \
                                   workspacePath + " -application " + application + " " + arguments)
                                   
def ImportCCS61Project(workspacePath, projectFolder):
    """This function..."""
    return _InvokeCCS61(workspacePath, "com.ti.ccstudio.apps.projectImport", "-ccs.location " + \
                        os.path.abspath(projectFolder), "")

def BuildCCS61Project(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeCCS61(workspacePath, "com.ti.ccstudio.apps.projectBuild", "-ccs.projects " + \
                        projectName + " -ccs.configuration " + projectConfig + " -ccs.buildType incremental", \
                        injectPrefix)   

def RebuildCCS61Project(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeCCS61(workspacePath, "com.ti.ccstudio.apps.projectBuild", "-ccs.projects " + \
                        projectName + " -ccs.configuration " + projectConfig + " -ccs.buildType full", injectPrefix)     

def CleanCCS61Project(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeCCS61(workspacePath, "com.ti.ccstudio.apps.projectBuild", "-ccs.projects " + \
                        projectName + " -ccs.configuration " + projectConfig + " -ccs.buildType clean", injectPrefix)                          

CCS53_DIR = eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("CCS53_PATH")

def _InvokeCCS53(workspacePath, application, arguments, injectPrefix):
    """This function..."""
    """ See http://processors.wiki.ti.com/index.php/Projects_-_Command_Line_Build/Create """
    return eduardomhg.CommandLine.Execute(injectPrefix + os.path.join(CCS53_DIR, "eclipsec") + " -noSplash -data " + \
                                   workspacePath + " -application " + application + " " + arguments)
                                   
def ImportCCS53Project(workspacePath, projectFolder):
    """This function..."""
    return _InvokeCCS53(workspacePath, "com.ti.ccstudio.apps.projectImport", "-ccs.location " + \
                        os.path.abspath(projectFolder), "")

def BuildCCS53Project(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeCCS53(workspacePath, "com.ti.ccstudio.apps.projectBuild", "-ccs.projects " + \
                        projectName + " -ccs.configuration " + projectConfig + " -ccs.buildType incremental", \
                        injectPrefix)   

def RebuildCCS53Project(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeCCS53(workspacePath, "com.ti.ccstudio.apps.projectBuild", "-ccs.projects " + \
                        projectName + " -ccs.configuration " + projectConfig + " -ccs.buildType full", injectPrefix)     

def CleanCCS53Project(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeCCS53(workspacePath, "com.ti.ccstudio.apps.projectBuild", "-ccs.projects " + \
                        projectName + " -ccs.configuration " + projectConfig + " -ccs.buildType clean", injectPrefix)                             
                        
### CODE WARRIOR ###   

CODEWARRIOR104_DIR = eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("CW104_PATH")
CODEWARRIOR106_DIR = eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("CW106_PATH")

def _InvokeCodeWarrior(codWarriorDir, projectPath, targets, projectConfig, injectPrefix):
    """This function..."""
    code = eduardomhg.CommandLine.Execute('"' + os.path.join(codWarriorDir, "eclipse\ecd.exe") + '"' + \
                                   " -generateMakefiles -project " + projectPath)
    if code == 0:
        origWD = os.getcwd()
        os.chdir(os.path.join(os.path.abspath(projectPath), projectConfig))
        code = eduardomhg.CommandLine.Execute(injectPrefix + '"' + os.path.join(codWarriorDir, "gnu/bin/mingw32-make.exe") + '"' +\
                                       " " + targets)
        os.chdir(origWD)
    return code

def CleanCW104Project(projectPath, projectConfig, injectPrefix = ""):
    """This function..."""
    buildDir = os.path.join(projectPath, projectConfig)
    print "Deleting " + buildDir + " directory..."
    if os.path.exists(buildDir):
        shutil.rmtree(buildDir)
    return 0
    
def CleanCW106Project(projectPath, projectConfig, injectPrefix = ""):
    """This function..."""
    buildDir = os.path.join(projectPath, projectConfig)
    print "Deleting " + buildDir + " directory..."
    if os.path.exists(buildDir):
        shutil.rmtree(buildDir)
    return 0    
                                       
def RebuildCW104Project(projectPath, projectConfig, injectPrefix = ""):
    """This function..."""
    buildDir = os.path.join(projectPath, projectConfig)
    print "Deleting " + buildDir + " directory..."
    if os.path.exists(buildDir):
        shutil.rmtree(buildDir)
    return _InvokeCodeWarrior(CODEWARRIOR104_DIR, projectPath, "all", projectConfig, injectPrefix) 

def RebuildCW106Project(projectPath, projectConfig, injectPrefix = ""):
    """This function..."""
    buildDir = os.path.join(projectPath, projectConfig)
    print "Deleting " + buildDir + " directory..."
    if os.path.exists(buildDir):
        shutil.rmtree(buildDir)
    return _InvokeCodeWarrior(CODEWARRIOR106_DIR, projectPath, "all", projectConfig, injectPrefix)
    
def BuildCW104Project(projectPath, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeCodeWarrior(CODEWARRIOR104_DIR, projectPath, "all", projectConfig, injectPrefix)
    
def BuildCW106Project(projectPath, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeCodeWarrior(CODEWARRIOR106_DIR, projectPath, "all", projectConfig, injectPrefix)     

### VISUAL STUDIO ###   

if (eduardomhg.EnvironmentVariables.CheckEnvironmentVariableExists("VS100COMNTOOLS")):
    VS2010_DIR = os.path.join(eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("VS100COMNTOOLS"), "..\IDE")
if (eduardomhg.EnvironmentVariables.CheckEnvironmentVariableExists("VS110COMNTOOLS")):    
    VS2012_DIR = os.path.join(eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("VS110COMNTOOLS"), "..\IDE")
if (eduardomhg.EnvironmentVariables.CheckEnvironmentVariableExists("VS140COMNTOOLS")):    
    VS2015_DIR = os.path.join(eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("VS140COMNTOOLS"), "..\IDE")

def _InvokeVisualStudio(vsDir, projectFile, option, projectConfig, injectPrefix):
    """This function..."""
    return eduardomhg.CommandLine.Execute(injectPrefix + '"' + os.path.join(vsDir, "devenv.com") + '"' + " " + projectFile + " " + option + \
                                   " " + projectConfig)

def CleanVS2010Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2010_DIR, projectFile, "/Clean", projectConfig, injectPrefix)
    
def CleanVS2012Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2012_DIR, projectFile, "/Clean", projectConfig, injectPrefix)
    
def CleanVS2015Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2015_DIR, projectFile, "/Clean", projectConfig, injectPrefix)       
    
def BuildVS2010Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2010_DIR, projectFile, "/Build", projectConfig, injectPrefix)

def BuildVS2012Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2012_DIR, projectFile, "/Build", projectConfig, injectPrefix)
    
def BuildVS2015Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2015_DIR, projectFile, "/Build", projectConfig, injectPrefix)        

def RebuildVS2010Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2010_DIR, projectFile, "/Rebuild", projectConfig, injectPrefix) 

def RebuildVS2012Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2012_DIR, projectFile, "/Rebuild", projectConfig, injectPrefix)        
    
def RebuildVS2015Project(projectFile, projectConfig, injectPrefix = ""):
    """This function..."""
    return _InvokeVisualStudio(VS2015_DIR, projectFile, "/Rebuild", projectConfig, injectPrefix)         
    
def _RunVSUnitTests(vsDir, resultsFile, unitTestProjects):
    """This function..."""
    containers = ""
    for project in unitTestProjects:
        if not project.endswith(".dll"):
            containers = containers + "/testcontainer:" + project +  "\\bin\\Debug\\" + project + ".dll "
        else:
            containers = containers + "/testcontainer:" + project
    return eduardomhg.CommandLine.Execute('"' + os.path.join(vsDir, "MSTest.exe") + '"' + " " + \
                                   containers + " " + "/resultsfile:" + resultsFile)
    
def RunVS2010UnitTests(resultsFile, unitTestProjects):
    """This function..."""
    """WARNING: if VS2010 and VS2012 are both installed, MSTest for VS2010 will hang. Solution: install SP1 for VS2010: 
    http://www.microsoft.com/en-US/download/details.aspx?id=23691 """
    return _RunVSUnitTests(VS2010_DIR, resultsFile, unitTestProjects)
    
def RunVS2012UnitTests(resultsFile, unitTestProjects):
    """This function..."""
    return _RunVSUnitTests(VS2012_DIR, resultsFile, unitTestProjects)
    
def RunVS2015UnitTests(resultsFile, unitTestProjects):
    """This function..."""
    return _RunVSUnitTests(VS2015_DIR, resultsFile, unitTestProjects)    
    
def ConvertVSTestResultsToNUnitFormat(vsFileName, nUnitFileName):
    msxslPath = '"' + os.path.join(os.path.dirname(__file__), "msxsl.exe") + '"'
    xsltPath = '"' + os.path.join(os.path.dirname(__file__), "MSBuild-to-NUnit.xslt") + '"'
    return eduardomhg.CommandLine.Execute(msxslPath + ' "' + vsFileName + '" ' + xsltPath + ' -o "' + nUnitFileName + '"')


def RunNUnitTests(resultsFile, unitTestAssemblies):
    """This function..."""
    assemblies = ""
    for assembly in unitTestAssemblies:
        if not assembly.endswith(".dll"):
            assemblies = assemblies + " " + assembly + "\\bin\\Debug\\" + assembly + ".dll "
        else:
            assemblies = assemblies + " " + assembly
    return eduardomhg.CommandLine.Execute("nunit3-console" + " " + assemblies  + " --result=" + resultsFile + ";format=nunit2")

    
def RunVS2015CppUnitTests(unitTestAssemblies):
    """This function..."""
    assemblies = ""
    for assembly in unitTestAssemblies:
        if not assembly.endswith(".dll"):
            assemblies = assemblies + " " + assembly + "\\bin\\Debug\\" + assembly + ".dll "
        else:
            assemblies = assemblies + " " + assembly
    return eduardomhg.CommandLine.Execute('"' + os.path.join(VS2015_DIR, r"CommonExtensions\Microsoft\TestWindow\vstest.console.exe") + \
                                   '"' + " " + assemblies + " " + "/logger:trx")
    
    
def GenerateVSDocumentation(vsSandcastleProjectFileName):
    return eduardomhg.CommandLine.Execute(r"c:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe " + \
                            vsSandcastleProjectFileName)    

### KEIL UVISION ###   

KEILUV5_DIR = eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("KEILUV5_PATH")

def _InvokeKeilUVision(projectFile, target, command):
    """This function..."""
    code = eduardomhg.CommandLine.ExecuteAndWait(os.path.join(KEILUV5_DIR, "UV4") +\
                                          " " + command + " " + projectFile + ' -t"' + target + '" -j0' + 
                                          " -o " + "keilLog.txt")
                                          
    print "Contents of the Keil log file:"                                                
    print
    
    with open("keilLog.txt", "r") as logFile:
        print logFile.read()
    print
    return code
                                                                            
def _InvokeKeilUVisionGeneratedBat(batFile, injectPrefix):
    """This function..."""
    return eduardomhg.CommandLine.Execute(injectPrefix + batFile)                                   
                                   
def BuildKeilUVisionProject(projectName, target, recompileWithBat = False, injectPrefix = ""):

    EXIT_CODES = { 0 : "No Errors or Warnings",
                   1 : "Warnings Only",
                   2 : "Errors",
                   3 : "Fatal Errors",
                   11 : "Cannot open project file for writing",
                   12 : "Device with given name in not found in database",
                   13 : "Error writing project file",
                   15 : "Error reading import XML file" }

    """This function..."""
    code = _InvokeKeilUVision(projectName + ".uvprojx", target, "-b")
    print "Exit code = " + str(code) + " (" + EXIT_CODES[code] + ")"

    if (code == 0) or (code == 1): # No errors, at most warnings
        if recompileWithBat:
            # Invoke generated .bat (the option must be enabled in the UVision project)
            # The only way to inject to Klocwork!
            batCode = _InvokeKeilUVisionGeneratedBat(target + '.bat', injectPrefix)
        else:
            batCode = 0
        return batCode
    return code
    
def CleanKeilUVisionProject(projectName, target):

    """This function..."""
    return _InvokeKeilUVision(projectName + ".uvprojx", target, "-c")

### DOXYGEN ###   

if (eduardomhg.EnvironmentVariables.CheckEnvironmentVariableExists("DOXYGEN1810_PATH")):
    DOXYGEN_DIR = os.path.join(eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("DOXYGEN1810_PATH"), "bin")

def _InvokeDoxygen(doxyFile):
    """This function..."""
    return eduardomhg.CommandLine.Execute(os.path.join(DOXYGEN_DIR, "doxygen") + " " + doxyFile)

def _ProcessDoxygenWarningsFile(file):
    """This function..."""
    with open(file) as f:
        lines = f.readlines()
    print "\nTOTAL WARNINGS FOUND: " + str(len(lines)/2) + "\n"
    return len(lines)/2 # Warnings are separated with a newline
    
def GenerateDoxygenDocumentation(doxyFile, warningsLogFile):
    """This function..."""    
    code = _InvokeDoxygen(doxyFile)
    if code == 0:
        code = _ProcessDoxygenWarningsFile(warningsLogFile)
    return code        

    
### ECLIPSE (CDT) ###    

ECLIPSE_DIR = eduardomhg.EnvironmentVariables.ReadEnvironmentVariable("ECLIPSE_PATH")
                                   
def ImportEclipseProject(workspacePath, projectFolder, injectPrefix = ""):
    """This function..."""
    return eduardomhg.CommandLine.Execute(injectPrefix + os.path.join(ECLIPSE_DIR, "eclipse") + " --launcher.suppressErrors " + \
                                   "-nosplash " + "-application org.eclipse.cdt.managedbuilder.core.headlessbuild " + \
                                   "-data " + workspacePath + " -import " + projectFolder)

def ImportEclipseProjects(workspacePath, projectFolders, injectPrefix = ""):
    """This function..."""
    cmd = injectPrefix + os.path.join(ECLIPSE_DIR, "eclipse") + " --launcher.suppressErrors " + \
                                   "-nosplash " + "-application org.eclipse.cdt.managedbuilder.core.headlessbuild " + \
                                   "-data " + workspacePath
    for folder in projectFolders:
        cmd = cmd + " -import " + folder                               
    return eduardomhg.CommandLine.Execute(cmd)    

def BuildEclipseProject(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return eduardomhg.CommandLine.Execute(injectPrefix + os.path.join(ECLIPSE_DIR, "eclipse") + " --launcher.suppressErrors " + \
                                   "-nosplash " + "-application org.eclipse.cdt.managedbuilder.core.headlessbuild " + \
                                   "-data " + workspacePath + " -build " + projectName + "/" + projectConfig)


def BuildEclipseProjects(workspacePath, projectNames, projectConfig, injectPrefix = ""):
    """This function..."""
    cmd  = injectPrefix + os.path.join(ECLIPSE_DIR, "eclipse") + " --launcher.suppressErrors " + \
                                   "-nosplash " + "-application org.eclipse.cdt.managedbuilder.core.headlessbuild " + \
                                   "-data " + workspacePath

    for projectName in projectNames:
        cmd = cmd + " -build " + projectName + "/" + projectConfig

    return eduardomhg.CommandLine.Execute(cmd)    

def RebuildEclipseProject(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return eduardomhg.CommandLine.Execute(injectPrefix + os.path.join(ECLIPSE_DIR, "eclipse") + " --launcher.suppressErrors " + \
                                   "-nosplash " + "-application org.eclipse.cdt.managedbuilder.core.headlessbuild " + \
                                   "-data " + workspacePath + " -rebuild " + projectName + "/" + projectConfig)

def CleanEclipseProject(workspacePath, projectName, projectConfig, injectPrefix = ""):
    """This function..."""
    return eduardomhg.CommandLine.Execute(injectPrefix + os.path.join(ECLIPSE_DIR, "eclipse") + " --launcher.suppressErrors " + \
                                   "-nosplash " + "-application org.eclipse.cdt.managedbuilder.core.headlessbuild " + \
                                   "-data " + workspacePath + " -clean " + projectName + "/" + projectConfig)

### QT CREATOR (QMAKE) ###    
                                   
def BuildQtProject(qmakePath, makePath, projectFilePath, options, outputRelativePath):
    """This function..."""
    (projectDir, projectName) = os.path.split(projectFilePath)

    outputDir = os.path.join(projectDir, outputRelativePath)
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    exitCode = 0
    if os.path.exists(os.path.join(outputDir, "Makefile")):        
        exitCode = eduardomhg.CommandLine.Execute(makePath + " -j4 clean", outputDir)
    if exitCode == 0:    
        exitCode = eduardomhg.CommandLine.Execute(qmakePath + " " + projectFilePath + " " + options, outputDir)
        if exitCode == 0:
            exitCode = eduardomhg.CommandLine.Execute(makePath + " -j4", outputDir)
    return exitCode
    
# This only executes if this script has been directly from the command line (not imported from another script).
if __name__ == '__main__':
    eduardomhg.Utilities.PrintInvalidModuleUsage(__doc__)
  