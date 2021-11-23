# Code Written By Subhojit Ghimire
# Make sure to cite as [https://github.com/GhimireSubhojit/Data-Preprocessing] when used this code format or reference anywhere in your project.

# Data Preprocessing for Excel CSV Files
# Generating Output of thousands of csv data in row-wise format
# Given Two Columns- First Column: File_Name or Article_Name. Second Column: Text_Data
# Output: First Row First Column: File_Name. Second Column: Text_Data_1
# Output: Second Row First Column: File_Name. Second Column: Text_Data_2 and so on for all thousands of rows

# EXAMPLE:
# test_data_0.csv
#   DOC     TEXT
#   doc1    Hello World | This is a Test Data | To show the working of this program
#   doc2    This is continuation | This is second row data
#   doc3    Unlinke the first two rows    This Data is separated by multiple spaces    This is an example

# After running the code
# output_test_data.csv
#   DOC     TEXT
#   doc1    Hello World
#   doc1    This is a Test Data
#   doc1    To show the working of this program
#   doc2    This is continuation
#   doc2    This is second row data
#   doc3    Unlike the first two rows
#   doc3    This Data is separated by multiple spaces
#   doc3    This is an example

import csv


# reading original csv file to work on.
with open ('test_data_0.csv') as csvFile:
    # opening output file to write on. Make sure you manually create output_test_data.csv file.
    with open ('output_test_data.csv', 'wb') as outFile:
        # Reads All the data of original csv file and stores in "data" variable.
        data = csv.DictReader (csvFile)
        # defininf the title/header, i.e., column names. The very first row has column names.
        # This array field can be modified to accomodate more or less column names as required.
        fieldNames = ['DOCNO', 'TEXT']
        # defining format for writing on csv output file.
        writer = csv.DictWriter (outFile, fieldnames = fieldNames)
        for ii in data:
            # docNo and txt are two string variables here. More string variables can be defined as required by the csv file (i.e., if more columns)
            docNo = ii['DOCNO']
            txt = ii['TEXT']
            length = len(txt)
            print (length)
            print ("\n")
            print (docNo)
            print (txt)
            newtxt = ""
            jj = 0
            txt = txt + "    \n"
            while jj < length:
                newtxt = newtxt + txt[jj]
                if (txt[jj] == '\n'):
                    break
                # The following if statement checks for either three consecutive spaces or one bar as the delimiters.
                # The statement can be modified to accomodate new separators/delimiters like commas, periods, etc. as required by the csv file.
                if ((txt[jj]==' ' and txt [jj+1]==' ' and txt [jj+2]==' ') or (txt[jj+1]=='|')):
                    # if the newtxt is not empty, then only print. otherwise skip printing empty lines.
                    if (newtxt.isspace() == False):
                        # writerow arguments can be modified to add more column types as required by the csv file.
                        writer.writerow ({'DOCNO': docNo, 'TEXT': newtxt})
                        print (docNo)
                        print (newtxt)
                        newtxt = ""
                        jj = jj+2
                jj = jj+1

