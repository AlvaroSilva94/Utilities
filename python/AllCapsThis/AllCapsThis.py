#-------------------------------------------------------------------------------------------
# Purpose: Python script to change all files in a folder to upper/lower case
#
# Usage example:
#   python AllCapsThis.py
#   - the script will then prompt the user to give as input:
#       - Upper or Lower case desired
# Notes:
#   The script has to be in the same folder as the files to rename     
#
# - Tested in Windows environment with Python 3.9.10 
#
# Modification History:
# CR        Date           Name           Comment
# --------  ------------   ------------   ------------------------------------------------------
# 0000      04/01/2022     Alvaro Silva   Initial version
#-----------------------------------------------------------------------------------------------

import os
import itertools

# Initializations and Template file paths
FileList = []
ActualName = []
AllCapsName = []
LowCapsName = []
path_to_dir = os.getcwd() #This directory

while True:
    Intended = input("Do you want to change to upper or lower cases? (U/L): ")
    if Intended not in ('U', 'L'):
        print("Please select \"U\" or \"L\".")
    else:
        break

#read file names in the directory
# r=root, d=directories, f = file_paths
for r, d, f in os.walk(path_to_dir):
    for file in f:
        if '.c' in file:
              FileList.append(file)
              #now remove .c to have only the string
              NameOnly = file.replace(".c","")
              ActualName.append(NameOnly)

#Get the upper and the lower names
for name in ActualName:
      name1 = name.upper()
      name2 = name.lower()
      AllCapsName.append(name1)
      LowCapsName.append(name2)

def toUpperCase():
    
    #Replace inside the file
    count_updated_files = 0

    for (name, upperName, eachFile) in itertools.zip_longest(ActualName, AllCapsName, FileList):       
        # the values to be replaced exist
        repl_tag_found = True
        #open file in read mode
        configFile = open(eachFile,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data = configFile.read()
        #replace the values in data
        data = data.replace(name,upperName)
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(eachFile,"w+", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data)
        #close file
        configFile.close()
        #Delete old file, create new one with updated name and count updated files
        os.remove(eachFile)
        with open(upperName + ".c", "a+", newline='') as new_cfile:
            new_cfile.write(data)
            new_cfile.close()

        count_updated_files+= 1

    print("Files updated: ",count_updated_files/2)

def toLowerCase():
    
    #Replace inside the file
    count_updated_files = 0

    for (name, lowerName, eachFile) in itertools.zip_longest(ActualName, LowCapsName, FileList):       
        # the values to be replaced exist
        repl_tag_found = True
        #open file in read mode
        configFile = open(eachFile,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data = configFile.read()
        #replace the values in data
        data = data.replace(name,lowerName)
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(eachFile,"w+", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data)
        #close file
        configFile.close()
        #Delete old file, create new one with updated name and count updated files
        os.remove(eachFile)
        with open(lowerName + ".c", "a+", newline='') as new_cfile:
            new_cfile.write(data)
            new_cfile.close()

        count_updated_files+= 1
        
    print("Files updated: ",count_updated_files/2)


if Intended =="U":
    {
        toUpperCase()
    }
elif Intended == "L":
    {
        toLowerCase()
    }


