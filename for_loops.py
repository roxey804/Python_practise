# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:40:31 2019

@author: 612436075
"""
#-------------FOR LOOPS-----------#

#How can i iterate over and view all the items in my list?
def fruit_loop():
    mylist = ["apple", "pear", "banana"]   
    for item in mylist:
        print( item)
        
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