# -*- coding: utf-8 -*-
"""
Python lists are a combination of heterogenouse elements e.g. a mixture of ints, strings and more lists!
"""

#----------------------LISTS----------------#

#-------------Adding to a list------------#
list1 = [1,2,3]
print("list1:", list1)
list2 = ["a", "b"]
print("list2:", list2)

list3 = list1 + list2
print("list3", list3)

#This adds the lists in order

#-------------appending or inserting items------------#
#use the append() method to add items to the end of the list
#use insert() method

#insert(index, item)

list3.insert(0,99)  #inserts 99 to the 0th index
print(list3)

#-------------Sorting------------#

#sort method

a_list = [1,7,3,8,4,6,6,20]

a_list.sort()