# -*- coding: utf-8 -*-
import time as t

"""
Python lists are a combination of heterogenous elements e.g. a mixture of ints, strings and more lists!

-Lists always start with an index of 0 with the last element being index -1
"""
#----------------------LISTS----------------#


list1 = [1,2,3]
print("list1:", list1)
list2 = ["a", "b"]
print("list2:", list2)

print("Accessing items in a list:")
t.sleep(2)

#-------------Accessing items in a list------------#
list2 = ["a","b","c"]
#for the first (0th index) item do:
list2[0]
#List of lists
list_of_lists = [[["a","b","c"]],[1,2,3]]
print(list_of_lists[0][0],list_of_lists[1][0])

#the LAST item can always be accessed using mylist[-1] or len(mylist) -1
#-------------Adding to a list or concatenating multiple lists------------#
print("Adding items to a list:")
t.sleep(2)
list3 = list1 + list2
print("list3", list3)

#This adds the lists in order


#list4 = list3 + 2
#print("list4:", list4)

#TypeError: This will not work as you cannot add ints to a list "can only concatenate list (not "int") to list"


#-------------Appending or inserting items------------#

#use the append() method to add items to the end of the list
#The append() method adds a single item to the existing list. It doesn't return a new list; rather it modifies the original list.
#Example: .append(int) or .append("string") or .append(another_list)
list4=[0]
list5 = list4.append(2)
print("list4: ",list4)

#use insert() method to insert items to a specified position 

# e.g.: insert(index, item)

list3.insert(0,99)  #inserts 99 to the 0th index
print(list3)


#-----------Removing from a list -----------------#
print("\n","Removing items from a list")

list6 = [2,3,4,55,6]
print(list6)

print("using the .remove attribute")
#.remove(x)
#this removes x from the list, if there are multipe, it will remove the FIRST instance of x
list6.remove(55)

#del(x) removes the item with INDEX x
print("using the del() method")

'''del(mylist[index_of_item_2b_removed])'''

print(list6)

#The .clear() clears the list from all its items

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

#--------------List assignment------#

'''if you have 2 lists with the same object e.g. a=[1] and b=[1], they will NOT refer to the same object. they may have the same value (== equality operator would result in True) but is (which checks if they are the same object) would result in False. 
see https://www.geeksforgeeks.org/difference-operator-python/'''

lista=[1]
listb=[1]
listc=lista #this results in lista being THE SAME OBJECT as listc, hence, if you edit listc, lista will change too!
