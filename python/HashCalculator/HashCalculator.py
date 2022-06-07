#--------------------------------------------------------------------------------
# Purpose: Simple utility script to calculate a message hash of an inputed file.
#
# Use: python HashCalculator.py -f <file>
#
# Modification History:
# CR        Date           Name           Comment
# --------  ------------   ------------   ---------------------------------------
# 0000      29/01/2022     amsilva       Initial version
#--------------------------------------------------------------------------------

# import the library module
import hashlib
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="InputFile", help="File to be read for the calculation")

args = parser.parse_args()
file = args.InputFile

# initialize a string
str = open(file, "r")
 
#read whole file to a string
data = str.read()
 
# encode the string
encoded_str = data.encode()
 
# create a sha1 hash object initialized with the encoded string
hash_obj = hashlib.sha1(encoded_str)
 
# convert the hash object to a hexadecimal value
hexa_value = hash_obj.hexdigest()
 
# print
print("Calculated message hash: \n", hexa_value)