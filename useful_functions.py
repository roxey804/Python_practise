# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:43:35 2019

@author: rnikoo
"""

#Split list to int

def split_list_to_int():
    mylist = [1,2,3]
    newlist = [int(d) for d in str(mylist)]
    print (newlist)
split_list_to_int()