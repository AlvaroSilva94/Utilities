#-------------------------------------------------------------------------------------------
# Purpose: Utility to replace broker values and recalculate crc
#
# Input  : "ReplaceBrokerValue.py -d <config-files-dir>"
#
# Notes  :
#         - The first value requested is the value for the current configuration that
#           we want to change. The second value requested is the value of where we want the
#           files to run.
#
# Modification History:
# CR        Date           Name           Comment
# --------  ------------   ------------   --------------------------------------------------
# 0000      26/05/2022     amsilva        Initial version
#-------------------------------------------------------------------------------------------

import os
from argparse import ArgumentParser
from tkinter import W
from crc import CrcCalculator, Configuration

def crc_calculation(contents):

    #set CRC calculation configuration as per RIA-SSRS-CNF-0020
    width           = 32
    poly            = 0xF4ACFB13
    init_value      = 0xFFFFFFFF
    final_xor_value = 0x00
    reverse_input   = True
    reverse_output  = True
    #other settings
    use_table = True
    #CRC Calculation proper
    conf = Configuration(width, poly, init_value, final_xor_value, reverse_input, reverse_output)
    crc_calculator = CrcCalculator(conf, use_table)
    crc = crc_calculator.calculate_checksum(contents)
    return crc

#Ask the user for the environment in which the files will be used
print("\n")
place = input("Enter where auxiliary configuration files will be used (local/remote/lab) \n")
oldplace = input(("Enter where auxiliary configuration files were used before (local/remote) \n"))
print("\n")

count_updated_files = 0
count_crc_calculated_files = 0

parser = ArgumentParser()
parser.add_argument("-d", dest="Directory", help="Path to root directory containing the configuration files")
args = parser.parse_args()

if args.Directory is not None:
    path_to_dir = args.Directory

else:
    path_to_dir = os.getcwd()

# get list of all files to make changes (recursively)
file_paths = []
# r=root, d=directories, f = file_paths
for r, d, f in os.walk(path_to_dir):
    for file in f:
        if '.xml' in file:
            file_paths.append(os.path.join(r, file))

# go through all files and make changes
for path in file_paths:

    #Tags for all found values as false
    repl_tag_found = False
    repl_tag2_found = False
    repl_tag3_found = False
    repl_tag4_found = False

    #For changes from remote to local 
    if place == "local" and oldplace == "remote":
        # the values to be replaced exist
        repl_tag_found = True

        #For the first broker the following will be done:
        #open file in read mode
        configFile = open(path,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data = configFile.read()
        #replace the values in data
        data = data.replace('10.42.34.69','172.18.0.4')
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(path,"wt", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data)
        #close file
        configFile.close()

        #For the second broker the following will be done:
        #open file in read mode
        configFile = open(path,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data2 = configFile.read()
        #replace the values in data
        data2 = data2.replace('10.42.34.71','172.18.0.5')
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(path,"wt", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data2)
        #close file
        configFile.close()

        count_updated_files += 1 

        #open changed file for the crc calculation
        configFile = open(path, "rb")
        #read data as bytes
        data3 = configFile.read()
        #Calculate CRC
        crcCalc = crc_calculation(data3)
        #open respective .crc file
        fs = open(path.replace(".xml", ".crc") , "wt", newline='\n' , encoding = "utf-8")
        #convert crc from int to string
        strCrc = str(crcCalc)
        #write crc value in .crc file
        fs.write(strCrc)
        #update calculated file var
        count_crc_calculated_files += 1

        # close current config file
        configFile.close()
 
     
#-----------------------------------------------------------------------------------------
    #For changes from remote to local 
    elif place == "remote" and oldplace == "local":
        # the values to be replaced exist
        repl_tag2_found = True

        #For the first broker the following will be done:
        #open file in read mode
        configFile = open(path,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data = configFile.read()
        #replace the values in data
        data = data.replace('172.18.0.4','10.42.34.69')
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(path,"wt", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data)
        #close file
        configFile.close()

        #For the second broker the following will be done:
        #open file in read mode
        configFile = open(path,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data2 = configFile.read()
        #replace the values in data
        data2 = data2.replace('172.18.0.5','10.42.34.71')
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(path,"wt", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data2)
        #close file
        configFile.close()
        # configFile = open(path,"rt")

        count_updated_files += 1  

        #open changed file for the crc calculation
        configFile = open(path, "rb")
        #read data as bytes
        data3 = configFile.read()
        #Calculate CRC
        crcCalc = crc_calculation(data3)
        #open respective .crc file
        fs = open(path.replace(".xml", ".crc") , "wt", newline='\n' , encoding = "utf-8")
        #convert crc from int to string
        strCrc = str(crcCalc)
        #write crc value in .crc file
        fs.write(strCrc)
        #update calculated file var
        count_crc_calculated_files += 1
    
        # close current config file
        configFile.close()
 

# #-----------------------------------------------------------------------------------------
    #For changes from remote to local 
    elif place == "lab" and oldplace == "local":
        # the values to be replaced exist
        repl_tag3_found = True

        #For the first broker the following will be done:
        #open file in read mode
        configFile = open(path,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data = configFile.read()
        #replace the values in data
        data = data.replace('172.18.0.4','10.61.1.25')
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(path,"wt", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data)
        #close file
        configFile.close()

        #For the second broker the following will be done:
        #open file in read mode
        configFile = open(path,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data2 = configFile.read()
        #replace the values in data
        data2 = data2.replace('172.18.0.5','10.61.1.27')
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(path,"wt", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data2)
        #close file
        configFile.close()
        # configFile = open(path,"rt")

        count_updated_files += 1

        #open changed file for the crc calculation
        configFile = open(path, "rb")
        #read data as bytes
        data3 = configFile.read()
        #Calculate CRC
        crcCalc = crc_calculation(data3)
        #open respective .crc file
        fs = open(path.replace(".xml", ".crc") , "wt", newline='\n' , encoding = "utf-8")
        #convert crc from int to string
        strCrc = str(crcCalc)
        #write crc value in .crc file
        fs.write(strCrc)
        #update calculated file var
        count_crc_calculated_files += 1
    
        # close current config file
        configFile.close()
 
# #-----------------------------------------------------------------------------------------
    #For changes from remote to local 
    elif place == "lab" and oldplace == "remote":
        # the values to be replaced exist
        repl_tag4_found = True

        #For the first broker the following will be done:
        #open file in read mode
        configFile = open(path,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data = configFile.read()
        #replace the values in data
        data = data.replace('10.42.34.69', '10.61.1.25')
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(path,"wt", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data)
        #close file
        configFile.close()

        #For the second broker the following will be done:
        #open file in read mode
        configFile = open(path,"rt", newline='\n' , encoding = "utf-8")
        #read config file into data
        data2 = configFile.read()
        #replace the values in data
        data2 = data2.replace('10.42.34.71','10.61.1.27')
        #close file
        configFile.close()
        #open file in write mode
        configFile = open(path,"wt", newline='\n' , encoding = "utf-8")
        #write the replacement into the file
        configFile.write(data2)
        #close file
        configFile.close()
        # configFile = open(path,"rt")

        count_updated_files += 1  

        #open changed file for the crc calculation
        configFile = open(path, "rb")
        #read data as bytes
        data3 = configFile.read()
        #Calculate CRC
        crcCalc = crc_calculation(data3)
        #open respective .crc file
        fs = open(path.replace(".xml", ".crc") , "wt", newline='\n' , encoding = "utf-8")
        #convert crc from int to string
        strCrc = str(crcCalc)
        #write crc value in .crc file
        fs.write(strCrc)
        #update calculated file var
        count_crc_calculated_files += 1
    
        # close current config file
        configFile.close()

    else:
        print("Value inputed for local/remote/lab not valid!")
 
#-----------------------------------------------------------------------------------------

    if repl_tag_found or repl_tag2_found or repl_tag3_found or repl_tag4_found:
        #print result
        print("Replacement of both broker values and crc calculation successfull for path: \n" + path)
        print("Calculated CRC: " + strCrc + "\n")
    else:
        print("Values for broker not found" + path)

# changes were made, on to the next fie
print("Number of updated files: " + str(count_updated_files) + "\n")    

# changes were made, on to the next fie
print("CRC calculated for: " + str(count_crc_calculated_files) + " files" + "\n")  