#--------------------------------------------------------------------------------
# Purpose: Simple utility script to add contents to a selected file. It also adds
#          recursively to all files inside a folder and calculates the CRC32 of
#          all those files.
#
# Use: python AddFileContentsAfterElement.py -d <path>
#
# Modification History:
# CR        Date           Name           Comment
# --------  ------------   ------------   ---------------------------------------
# 0000      16/05/2022     amsilva       Initial version
#--------------------------------------------------------------------------------

import os
from argparse import ArgumentParser
from crc import CrcCalculator, Configuration

def crc_calculation(contents):
    """
    Just to calculate the crc
    """
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

#Updated files counter 
count_updated_files = 0

#to get path passed from command line with "-d path"
parser = ArgumentParser()
parser.add_argument("-d", dest="Directory", help="Path to root directory containing the configuration files")
args = parser.parse_args()

#if directory is not null use directory, else use current directory
if args.Directory is not None:
    path_to_dir = args.Directory

else:
    path_to_dir = os.getcwd()

#Path to file in same folder
path_to_content = "FileContents.txt"

# get list of all files to make changes (recursively)
file_paths = []
# r=root, d=directories, f = file_paths
for r, d, f in os.walk(path_to_dir):
    for file in f:
        if '.xml' in file:
            file_paths.append(os.path.join(r, file))

# get text to append to file
with open(path_to_content) as f:
    content_lines = f.readlines()


# go through all files and make changes
for path in file_paths:
    tsr_tag_was_found = False
    config_file = open(path, "r+", newline='\n' , encoding = "utf-8")
    line_count = 0

    # get all lines from config file
    config_file_lines = config_file.readlines()

    # go through lines and find the TSR comment tag
    for line in config_file_lines:

        if (line.find("<!-- Example Line is here-->") != -1):
            tsr_tag_was_found = True
            
            # delete all contents of file
            config_file.truncate(0)
            # rewind file stream
            config_file.seek(0)
            # write contents until TSR element + new TSR element
            config_file.writelines(config_file_lines[0 : line_count] + content_lines)
            
            count_updated_files += 1
            #CRC functionality
            with open( path.replace(".xml", ".crc") , "w",
                newline='\n' , encoding = "utf-8") as fs:
                fs.write( str(crc_calculation(config_file.read())) )

            # changes were made, on to the next file
            break
            
        line_count += 1
    
    # close current config file
    config_file.close()

print("Number of updated files: " + str(count_updated_files))