import time

"""
-Simple if/else statements
-Ternary (one line) conditionals
if condition:
   do this
then continue here regardless
"""

print("\n ------if statements-----")

if 25<30:
    print("25 is less than 30")
#if this was not the case, the print block would NOT be executed

#double equals is used to check equality 
if not 25 == 26:
    print("they are not equal")

#note the difference between == and is
if 2 == 2.0:
    print("2 == 2.0")

if 2 is 2.0:
    print("2 is 2.0")
#2 is NOT 2.0 but is == to 2.0

print("\n ---------if var >> (if true)------")

#in python all non-zero values are considered True, hence, this works as "if true".. execute code

number=23
if number:
    print("this works as the var 'number' is  a non-zero value")
#try this with number = 0 :) 
print("\n ---------if and else statemements--------")
'''
if condition:
    do this
else:
   do something else
'''
salary = 1000
expenses = 500
within_budget = False
if salary-expenses>0:
    within_budget = True

print("am i within my budget?", within_budget)

def conditionals():
    result = "pass"
    if result == "pass":
        print("well done")
    else:
        print("sorry, better luck next time")

def example1():
    code = int(input("enter code: "))
    if code == 123:
        print("ok")
    print("goodbye")

def example2():
    code = int(input("enter code: "))
    if code == 123:
        print("ok")
    else:
        print("incorrect")
#example1()
        
#---------------Elif--------------#
def example3():
    code = int(input("guess the number:"))
    if code == 123:
        print("well done!")
    elif code <100:
        print("it's over 100")
    elif 101<code<122:
        print("nearly there")
    else:
        print("you've gone too far!")
        
#example3()        
        
def conditionals_2():
    mynum = 2
    result = True
    if mynum == 2 and result == True:
        print("passed")
#conditionals_2()
        
time.sleep(1)

print("Checking if we have an item in our list")

holiday_bag=["passport","money","phone"]
#Check if you've got your phone:

if "money" in holiday_bag:
    print("yes your money is in your holiday bag")
    
#or a one-liner type into Ipython:
"money" in holiday_bag

#---------------Ternary conditionals--------------#
print("\n------Ternary conditionals--------")      
'''remove the need for multiline statements'''

#condition_if_true IF condition ELSE condition_if_false

def ternary_conditionals():
    a = 1
    b = 2
    print("bigger") if a > b else print("smaller")

#ternary_conditionals()


#---------------Advanced flow control--------------#
    
'''else clauses on for and while loops'''


#while condition:
#    do this
#else:
#    do something else

'''the else block only evaluates when the while condition loop is false'''


#---------------For Else--------------#

#for item in iterable:
#    if match(item):
#        do this
#        break
#else: #no break, no match found
#    do something else
#    
#print(result)

'''In a given list [x,y,z] are any of the components dividible by 2?'''

number_list = [2,5,8,10]
divisor = 2
answers = []

def for_else():
    for item in number_list:
        if item % divisor == 0:
            result = "found"
            answers.append(item)
            
    else: #no break, no match found
        result = None
        
    print(result, answers)
    
'''However, loop-else are rather uncommon so best to refactor as below:'''

def is_divisible():
    for item in number_list:
        if item % divisor == 0:
            result = "found"
            answers.append(item)
    return answers,result
        
#is_divisible()
    

