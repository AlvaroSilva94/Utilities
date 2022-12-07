#-----------------------------------------------------------------------------
# Purpose: Generation of test case scripts with the complete structure, ready
# to implement the test logic, from the Doors export. This 
# script generates .c files for the specified test.
#
# Usage example:
#   python generate-tests.py
#   - the script will then prompt the user to give as input:
#       - The requirement to be tested;
#       - The user name;
# Notes:
#   The script expects the following files and directories to be present:
#       \output\                             -> folder to save the generated scripts
#       \template\cmocka-template.c          -> template for the .c files      
#
# - Tested in Windows environment with Python 3.9.10 
#
# Modification History:
# CR        Date           Name           Comment
# --------  ------------   ------------   ------------------------------------
# 0000      02/12/2022     Alvaro Silva   Initial version
#-----------------------------------------------------------------------------

from msilib.schema import ComboBox
import openpyxl
import os
import glob
from collections import namedtuple
import re
from datetime import datetime

# Template file paths
CMOCKA_TEMPLATE_NAME = "template\cmocka-template.c"
OUTPUT_DIR = "output\\"

# Getting the req as user input 
FIND_VALUE_NUM = input("Please input the desired requirement to be tested: ")
DOORS_EXPORT_PATH = input("Please enter the specified DOORS export (.xlsx) file path: ")

# String concatenation
BASE = "E600SWRS-"
FIND_VALUE = "".join((BASE, FIND_VALUE_NUM))  

C_BASE_FUNCT_NAME = "CT_GSTMCTRL_etcs_swrs_"
C_FUNCT_NAME = "".join((C_BASE_FUNCT_NAME,FIND_VALUE_NUM))

TEST_FILE_PREFIX = "ct_gstmctrl_etcs_swrs_"
TEST_FILE_POSTFIX = ".c"

TEST_FILE_PREFIX = "".join((TEST_FILE_PREFIX,FIND_VALUE_NUM))
TEST_FILE_NAME = "".join((TEST_FILE_PREFIX,TEST_FILE_POSTFIX))

#Named tuple to store the result of the values from excel
test_case_1 = namedtuple('test_case', ['test_case_id', 'componentName', 'fileNameC','coverage','requirementID', 'requirementTxt', 'functionFromReq'])

def getValuesFromExcelFile(file_path):
    file_path = os.path.abspath(file_path)
    tg_xlsx = openpyxl.load_workbook(file_path, read_only=True)

    #Values to be inserted in the tuple
    test_case_id = C_FUNCT_NAME
    fileNameC = TEST_FILE_NAME
    requirementID = FIND_VALUE
    requirementTxt = ""
    coverage = ""
    componentName = ""
    functionFromReq = ""

    #creating a tuple to store values
    test_case = namedtuple('test_case', ['test_case_id', 'componentName', 'fileNameC','coverage','requirementID', 'requirementTxt', 'functionFromReq'])

    #get data from test cases
    sheet_data = tg_xlsx['RichText']
    #num_rows = sheet_data.max_row

   #for row in num_rows():
    for row in sheet_data.iter_rows():
        for cell in row:
            if cell.value == requirementID:
                #Get requirement and function to test
                functionFromReq = sheet_data.cell(row=cell.row, column=15).value 
                requirementTxt = sheet_data.cell(row=cell.row, column=5).value 
                coverage = sheet_data.cell(row=cell.row, column=18).value
                componentName = sheet_data.cell(row=cell.row, column=13).value

    test_case = test_case(test_case_id, componentName, fileNameC, coverage, requirementID, requirementTxt, functionFromReq)

    return test_case

#create the .c file for each test case
def create_test_cmocka_template_c(template_path, test_case):
        
        #open template in read only mode, preserving LF
        with open(template_path, "r", newline='') as c_template_file:
            c_template_data = c_template_file.read()

            #replacing in the template file to create the new file
            c_new_file = re.sub('@fileNameC@', test_case.fileNameC, c_template_data)
            c_new_file = re.sub('@test_case_id@', test_case.test_case_id, c_new_file)
            c_new_file = re.sub('@componentName@',test_case.componentName, c_new_file)
            c_new_file = re.sub('@coverage@', test_case.coverage, c_new_file)
            c_new_file = re.sub('@requirement@', test_case.requirementID, c_new_file)
            c_new_file = re.sub('@requirementTxt@', test_case.requirementTxt, c_new_file)
            c_new_file = re.sub('@functionFromReq@', test_case.functionFromReq, c_new_file)

            #Note: Possibility to add date later
            #date_string = datetime.today().strftime('%d/%m/%Y')
            #c_new_file = re.sub('@date@', date_string , c_new_file)

            #generate .c file
            with open(OUTPUT_DIR + test_case.fileNameC, "w", newline='') as c_file:
                c_file.write(c_new_file)

def RemoveOldFiles():

    # Search files with .txt extension in current directory
    pattern = "*.c"
    OldTests = glob.glob(pattern)

    # deleting the files with txt extension
    for file in OldTests:
        os.remove(file)

print("Getting data from Doors export!")
#getValuesFromExcelFile(DOORS_EXPORT_PATH)
test_case_1 = getValuesFromExcelFile(DOORS_EXPORT_PATH)

print("Removing all files from output folder!")
RemoveOldFiles()

print("Generating .c file")
#create_test_cmocka_template_c(CMOCKA_TEMPLATE_NAME, getValuesFromExcelFile(DOORS_EXPORT_PATH))
create_test_cmocka_template_c(CMOCKA_TEMPLATE_NAME, test_case_1)

print("All done!")