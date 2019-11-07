# -*- coding: utf-8 -*-
"""
Given  a year, return the century that it is in e.g. for 100 return 1st century, for 1875 return 19th century, for 2000 return 20th century, for 2001 return 21st century. 
"""


#python sum sums digits in a list

def find_century(year):
    mylist = [int(d) for d in str(year)]
    print (mylist)
    if mylist[-2] == mylist[-1]:
        return version1(mylist, year)
    else:
        return version2(mylist, year)
    
def version1(mylist, year):
    print(mylist[:2])
    result = ''.join(map(str,newlist))
    century = int(result) 
    print("For the year", year,"century:", century)

def version2(mylist, year):
    print(mylist[:2])
    result = ''.join(map(str,newlist))
    century = int(result) + 1
    print("For the year", year,"century:", century)
    
find_century(101)   
    
#
#def get_first_2_digits():
#    print("newlist: ", mylist[:2])
#    newlist = mylist[:2]
#    result = ''.join(map(str,newlist))
#    print (int(result))
#    
 
'''Solutions:
    divide by 100 and then you get the first 2 digits!'''