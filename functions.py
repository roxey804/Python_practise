# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:15:09 2019

@author: rnikoo
"""

# -*- coding: utf-8 -*-
"""
For loops allow you to iterate over an object, this being a string, list, tuple or dictionary but NOT an int
"""
#-------------FOR LOOPS-----------#

#How can i iterate over and view all the items in my list?
def fruit_loop():
    mylist = ["apple", "pear", "banana"]   
    for item in mylist:
        print(item)
        
fruit_loop()


nums = [2,3,4]    
def is_divisible_by2():
    for number in nums:
        if number % 2 == 0 :
            return True
        return False
    
    
#how to loop over printing out the result each time?
        
nums = [2,3,4]    
def is_divisible_by2():
    for number in nums:
        if number % 2 == 0 :
            return True
        return False
'''Repeating a for loop n times e.g. Random number generator'''

def random_number_generator():
    import random
    for i in range(10):
        lottery_ticket = random.randint(1,100)
    print("your random number is:", lottery_ticket)
random_number_generator()        

 
'''For loop that moves up/down in specified steps '''

#using i in range
def move_in_steps():
    for i in range (START,STOP,STEP):
        print(i)
        
        
def move_in_steps():
    for i in range (2000,2015,2):
        print(i)
        
move_in_steps()

#------printing out the index of each item ----------#

print("\n for loop using enumerate to print out the index of each item ")

def index_loop():
    age = [12,24,32]
    for index, height in enumerate(age):
        print("index-" + str(index) + ": " + str(height))
#to start at index 1 just do index+1 :)
index_loop()

#------For x in range---------#
print("\n ------For x in range--------")
#range(x,y) x INclusive and y EXclusive

def for_in_range():
    for i in range(0,10):
        print(i)
for_in_range()

#to print sthing x times

def print_multiple_times():
    for i in range(5):
        print("i must do my homework")

print_multiple_times()


print("\n for loop with conditional")

def conditional_for():
    ages=[18,22,12,8,39,50,45,17]
    for age in ages:
        if age <18:
            print("Age", age, ": no entry")
        else:
            print("Age", age, ": entry permitted")

conditional_for()

#------Practical example of conditional for loop---------#
print("\n ------Task--------")
'''Calculate how many of group_a are under age and how many are allowed in to the club'''

def task():
    group_a=[18,22,12,8,39,50,45,17]
    over_18 = []
    under_age = []
    for age in group_a:
        if age <18:
            under_age.append(age)
            print("Age", age, ": no entry")
        else:
            over_18.append(age)
            print("Age", age, ": entry permitted")
    print("Over 18s:", len(over_18))
    print("Under age:", len(under_age))
task()

#----------one-liners---------#
#[ expression for item in list if conditional ]

print("\n ------Task using tidy list comprehensions---------")
def task_using_list_comprehension():
    group_a=[18,22,12,8,39,50,45,17]
    over_18 = [age for age  in group_a if age >=18 ]
    under_age = [age for age in group_a if age <18]
    
    print("Over 18s:", len(over_18))
    print("Under age:", len(under_age))

task_using_list_comprehension()


print("\n For loop iterating over dictionaries")

mydict = {"person1": "john", "person2": "julie", "person3":"mary"}

for k in mydict:
    print("keys:", k)

    #to print all keys:
for k in mydict.keys():
    print(k)
    
#to print all values:
for v in mydict.values():
    print(v)

#to print keys ANDvalues:
print("\n For loop iterating over dictionaries keys AND values")

for k in mydict:
    print(k, mydict[k])

#this gives a tuple 
print(mydict.items())

for k,v in mydict.items():
    print(k,v)
