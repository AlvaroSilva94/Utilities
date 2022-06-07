#----------------------------------------------------------------------------------
# Purpose: Simple utility to remove files from folders and add "deleteme.txt" to
#          to facilitate the commit of empty folders in git (that will be pupulated
#          later).
#
# Input  : Number of tests        -  Inputed directly in the cmd by user
# Input  : Test case        	  -  Inputed directly in the cmd by user
# Input  : <folders for the test> - Folders with the same name as Test case but
#									different TC.
# Output : <folders for the test> - Same folders as before but with content erased
#									and a "deleteme.txt" inside each folder.
#
# Notes  : 
# - The previously mentioned folders have to be placed inside folder "FoldersToPurge"
# - tested in windows environment with Python 3.10.0
# - usage example:
#   python deleteme.py
#
# Modification History
# CR        Date       Name        Comment  
# -------  ----------  --------  -----------------------------------------------------
# 0000	   15/01/2022  amsilva   Initial version
#-------------------------------------------------------------------------------------

import os
import subprocess
import shutil

#Input number of test-cases
TestCases = input("Please insert the number of testcases: \n")
#Convert from string to int
numberOfTestCases = int(TestCases)
testCaseIDmultiplier = 10
#Input the Test case string
testCaseString = input("Please input test case string: \n")
#Directory of the files to be purged
TC_directory = "FilesToPurge"
#Deleteme file to be placed inside the folders
filetopaste = "deleteme.txt "

for x in range(1, numberOfTestCases + 1):
    testCaseID = testCaseString + "_" + str(x * testCaseIDmultiplier).zfill(3)
    print(testCaseID)
    pathToCurrentTestDir2 =  TC_directory + "\\" + testCaseID
    print(pathToCurrentTestDir2)
    
	#Remove all the files in the directory
    for files in os.listdir(pathToCurrentTestDir2):
        path = os.path.join(pathToCurrentTestDir2, files)
        try:
           shutil.rmtree(path)
        except OSError:
           os.remove(path)
	   
    #Copy deleteme file to the respective folder
    shutil.copy(filetopaste, pathToCurrentTestDir2)
    print("Done, dummy files created\n")