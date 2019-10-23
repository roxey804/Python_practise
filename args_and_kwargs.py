# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:02:08 2019

@author: rnikoo
"""
import time

#---------------*ARGS AND **KWARGS -----------#

#Take an example of a simple add function: 

def add(x,y):
    result = x + y
    return result


print(add(4,3))

#we can imput any values and pass through the add function 

#however, print(add(4,3,2,1)) #would FAIL, giving a TypeError as we have specified 2 arguments but added 4. We can make this work using *args.
#*args will catch ALL our arguments. Let's try a modified function, add_2

def add_2(*args):
    result = 0
    for x in args:
        result += x
    return result

    
add_2(1,2,3)
#This now works!

def myfunc(*args):
    for arg in args:
        print(arg)
        
mylist = [1,2,3,4,"apple"]
myfunc(mylist) #returns the whole list, but what if we wanted EACH list item to be passed in INDIVIDUALLY?

myfunc(*mylist)
#will run through the list and pass each item individually  (because of the * )

#Generic example with a required argument "x" but aso accepting extra positional arguments (args) and key workd arguments (kwargs). 

def func(x, *args, **kwargs):
    print(x)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

#func()
#will raise a TypeError as it is missing the 1 required positional argument (x)
        
func("bla")

func("bla", 1,2)
#returns the first arg and also the positional arguments (1,2) as a tuple
func("bla",1,2, key1="val", key2="val2")
#now returns the key value pairs as a dictionary