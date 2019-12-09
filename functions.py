import time

"""
For loops allow you to iterate over an object, this being a string, list, tuple or dictionary but NOT an int
"""
#-------------FUNCTIONS-----------#

#----------Python in-built functions--------#

#print()
#len()
#sum()  calculates the sum of items in a list
#min(), max(), abs()

print("----------Create a python function--------")

def my_function_name():
    pass

#Invoking the function can be done adding ()
my_function_name()

'''Note, a function has to be DEFINED first, before it can be invoked'''
#Adding input arguments 

def addition(a,b,c):  #this func requires 3 input args a,b,c
    result = a +b +c
    print("sum is:", result)

addition(2,3,4)
#ensure you give 3 arguments when you invoke this function, as a test see what happens when you do with 2
#addition(2,3)

def exponential(number, power):
    result = number ** power
    print(result)

exponential(3,2) #this is basically 3^2

'''generally, functions should RETURN variables and not print them'''

def exponentials(num):
    square = num*num
    cube = num*num*num
    print("The square and cube will not be printed but returned as output")
    return square,cube  #this will be a tuple

exponentials(2)
#try running this in the Ipython console, will you see the result?