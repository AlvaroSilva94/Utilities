# Information

Due to confidential issues, the export file will not be included in this respository.
All other files are present.

## Script usage 

```
#-------------------------------------------------------------------------------------------
# Purpose: Generation of test case scripts with the complete structure, ready
# to implement the test logic, from the Doors export. This 
# script generates .c files for the specified test.
#
# Usage example:
#   python generate-tests.py
#   - the script will then prompt the user to give as input:
#       - The number of tests to be created;
#       - The requirement(s) to be tested;
#       - The path to the DOORs export file with .xlsx extension;
# Notes:
#   The script expects the following files and directories to be present:
#       \output\                             -> folder to save the generated scripts
#       \template\cmocka-template.c          -> template for the .c files      
#
# - Tested in Windows environment with Python 3.9.10 
#
# Modification History:
# CR        Date           Name           Comment
# --------  ------------   ------------   ------------------------------------------------------
# 0000      02/12/2022     Alvaro Silva   Initial version
# 0001      03/12/2022     Alvaro Silva   Added possibility to select multiple requirements
#                                         and create multiple test cases at once
# 0002      13/12/2022     Alvaro Silva   Added automatic date retrival and name input
# 0003      14/12/2022     Alvaro Silva   Added retrieval of data from plan.md
# 0004      14/12/2022     Alvaro Silva   Added config file to store name, export and plan paths
# 0005      22/12/2022     Alvaro Silva   Added option to never use plan if not needed
# 0006      22/12/2022     Alvaro Silva   Fixed dependance of fixed column structure
#-----------------------------------------------------------------------------------------------

```
