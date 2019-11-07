# -*- coding: utf-8 -*-
"""
Python lists are a combination of heterogenous elements e.g. a mixture of ints, strings and more lists!
"""
#----------------------LISTS----------------#


list1 = [1,2,3]
print("list1:", list1)
list2 = ["a", "b"]
print("list2:", list2)

#-------------Adding to a list------------#

list3 = list1 + list2
print("list3", list3)

#This adds the lists in order


#list4 = list3 + 2
#print("list4:", list4)

#TypeError: This will not work as you cannot add ints to a list "can only concatenate list (not "int") to list"


#-------------Appending or inserting items------------#

#use the append() method to add items to the end of the list
#The append() method adds a single item to the existing list. It doesn't return a new list; rather it modifies the original list.
list4=[0]
list5 = list4.append(2)
print("list4: ",list4)
#use insert() method to insert items to a specified position 

# e.g.: insert(index, item)

list3.insert(0,99)  #inserts 99 to the 0th index
print(list3)

print("\n")#-------------Sorting------------#

# .sort()   or  sorted()

# The .sort() function modifies the list in-place and has NO RETURN value. The list will be permanently changed.

#The sorted() function will create a NEW LIST containing a sorted version of the list it is given.

#.sort method   | myvar.sort()

a_list = [7,1,3,8,4,6,6,20]
print("a list:", a_list)
a_list.sort()
print("a list.sort():", a_list, )
print("a list:", a_list,"(permanently changed)")

#sorted()  method  |  sorted(myvar)
another_list=[6,2,8,4,20,14]
print("another list:", another_list)
print("sorted(another_list):", sorted(another_list))
print("another list:", another_list, " (it's back to the original)")

print("\n")#-------------Split list to int------------#


def list_to_int():
    mylist = [5,2,1]
    for i in mylist:
        print(i, type(i))
list_to_int()

#add an integer to every item in the list and return the new list
 
def list_to_int_addition():
    old_list = [5,2,1]
    new_list=[]
    for i in old_list:
        new_val=(i+1)
        new_list.append(new_val)
    print("old list:", old_list)
    print("new list:", new_list)

list_to_int_addition()      

#---------List comprehensions-----------#

#[ expression for item in list if conditional ]
#This is equivalent to:

#for item in list:
#    if conditional:
#        expression
        
def list_comprehension():
    old_list = [5,2,1]
    new_list= [i+1 for i in old_list]
    print("old list:", old_list)
    print("new list:", new_list)

list_comprehension()

def list_int_to_string():
    old_list = [5,2,1]
    new_list=[]
    for i in old_list:
        new_val=str(i)
        new_list.append(new_val)
    print("old list:", old_list)
    print("new list:", new_list)

list_int_to_string()  


#def split_list_to_int():
#    mylist = [1,2,"3"]
#    newlist = [int(d) for d in str(mylist)]
#    print (newlist)
#split_list_to_int()