# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:53:10 2019

@author: rnikoo
"""

import time
import csv 


#--------------Opening and reading txt Files With csv---------------------------#

#with open("filename.txt") as csv_file:
#    myCSV_var = csv.reader(csv_file, delimiter=",") #Comma separated val's
#    line_count = 0
#    for row in myCSV_var:
#        if line_count == 0:
#            print(f"column names are {", ".join(row)}")
#            line_count += 1
#        else:
#            print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.")
#            line_count += 1
#    print(f"Processed {line_count} lines.")
#    
#--------------Reading CSV Files With csv---------------------------#

#with open("employeebday.csv") as csvfile:
#    employeebday = csv.reader(csvfile, delimiter = ",")
#    print("We will now print out each row of the csv file, left to right using a For loop")
#    time.sleep(2)
#    print("for row in var, print row:")
#    time.sleep(2)
#    for row in employeebday:
#        time.sleep(2)
#        print(row) #if the output gives [] that indicates there is an EMPTY lINE in the file
##        print("printing row[0]:",row[0])
#        
#        #in order to run another FOR loop we have to open the file again as the cursor gets to the end and closes the file. A way to get over this, see 
#        
#with open("employeebday.csv") as csvfile:
#    employeebday = csv.reader(csvfile, delimiter = ",")
#    print("Now to run another FOR loop we need to tell python to open the file again, since it will STOP after the cursor goes to the end of the file. print row[0] will give the 1st item in the row, this will be 'Name' in row 0 and then 'John Smith' in row 1 and so on:")
#    time.sleep(4)
#    for row in employeebday:
#        print(row[0])


#--------------Read CSV example printing out statements about csv file contencts--------------#
#with open('employeebday.txt') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
#            line_count += 1
#        else:
#            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#            line_count += 1
#    print(f'Processed {line_count} lines.')
 
 
#----------------Print a specific row, one after another -------------#
def print_rows_in_order():
    with open("employeebday.csv") as csvfile:
        employeebday = csv.reader(csvfile, delimiter = ",")
        for row in employeebday:
            print(row) 
    with open("employeebday.csv") as csvfile: #we have to reopen the file again
        employeebday = csv.reader(csvfile, delimiter = ",")
        for row in employeebday:
            print(row[0])        
    
#print_rows_in_order()        
   
#---------Print a specific row, one after another in a function ---------------#
        
        def printspecificrow(x):
            with open("employeebday.csv") as csvfile:
                employeebday = csv.reader(csvfile, delimiter = ",")
                for row in employeebday:
                    if x == -1:
                        print(row)
                    else:
                        print(row[x])

#printthis(-1) #print all rows (print (row))
#printthis(x) #print items in position x of EACH ROW

#------------Viewing CSV files in a table ---------------#
            
#This requires DATAFRAMES from the PANDAS library so lets import pandas
                
import pandas

def open_csv_in_table():
    df = pandas.read_csv("employeebday.csv")
    print("This will print our CSV file as a table:")
    print(df)


open_csv_in_table()