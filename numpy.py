# -*- coding: utf-8 -*-
"""
NUMPY

First of all, numpy arrays cannot contain elements with different types. If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list. This is known as type coercion.

Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists than numpy arrays!.
"""

# Import numpy, now you can use its methods as np.method
import numpy as np
import time as t

#[row,col]
# regular list of lists

example = [[ 1, 0, 0],
            [ 0, 1, 2]]
example_array = np.array(example)

list_x = [["a","b"],["c","d"]]
#to access a and c in list_x you would do:
print(list_x[0][0],list_x[1][0])


print("converting it to a NumPy array:")
t.sleep(2)
#converting it to a NumPy array:
np_array = np.array(list_x)

#in the format [row, col] select all rows using : and the req'd column with the index, 0 for the first column, 1 for the second and so on. 
print(np_array[:,0])
#----------------NumPy attributes-------------------#


print("NumPy Attributes:")
t.sleep(2)
#.shape gives you information about the datastructure in the format [row, col]
print(".shape")
print(np_array.shape)

z = np.array([[1,2,3],
              [4,5,6]])
print(z[0:, 1:]) #returns the 1st and 2nd index in both rows ([0: is row 0 till the end so all rows, 1: is col index 1 to the end])
## Create the light array
#light = np.array(bmi<21)
#
#
## Print out light
#print(bmi[light])
#
#print(bmi <21)

#
#np.array([True, 1, 2]) + np.array([3, 4, False])
##True is converted to 1, False is converted to 0.
#>.array([4,5,2])