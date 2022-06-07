#--------------------------------------------------------------------------------
# Purpose: Simple utility script to remove numbers and _ in file names.
#
# Use: python NumberRemover.py
#
# Modification History:
# CR        Date           Name           Comment
# --------  ------------   ------------   ---------------------------------------
# 0000      16/06/2021     amsilva       Initial version
#--------------------------------------------------------------------------------

import glob
import os
import shutil

#get current directory and selected directory
directory = "\output"
currentPath = os.getcwd()

#Check if path exist, if not create folder
if not os.path.exists(currentPath + "\\" + directory):
    os.makedirs(currentPath + directory)

print("Modifying xml files names")

#iterate through files to find _ and remove _ and numbers after
for file in glob.glob("*.xml"):
    positionOfUnderscore = file.find("_")
    positionOfUnderscoreOld = 0
    auxfile = file[positionOfUnderscore + 1:]
    while positionOfUnderscore != -1:
        positionOfUnderscoreOld += positionOfUnderscore + 1
        positionOfUnderscore = auxfile.find("_")

        if positionOfUnderscoreOld != -1:
            auxfile = auxfile[positionOfUnderscore + 1:]

    if positionOfUnderscoreOld > 0:
        newfilename = file[:positionOfUnderscoreOld - 1]
        shutil.copy(currentPath + "\\" + file, currentPath + "\\" + directory + "\\" + newfilename + ".xml")
    else:
        print("Error. No underscore found!")

print("Done")
