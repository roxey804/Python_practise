import time


#-------------FUNCTIONS-----------#
'''PEP8 naming convention: Use a lowercase word or words. Separate words by underscores to improve readability e.g.	function, my_function'''
#Functions with multiple args:

#def function(arg_one, arg_two,
#             arg_three, arg_four):
#    return arg_one
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

'''Note, a function has to be DEFINED first, before it can be invoked. To invoke/call it type function_name() in the console, otherwise function_name will just return the type- Function object'''
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

'''variables OUTSIDE a function are called global variables and those INSIDE/WITHIN  a function are local/private specific to only that function'''

#Global vars:

var1='sunday'

def my_function():
    var1= 'monday'
    var2='tuesday'
    
    print("Local var1 and var2:", var1, var2)
    
#note the difference:

print("Global var1:", var1)
my_function()    
#--------------------------------------------#

colour1="black"    

def my_function2(colour1):
    colour1="blue"
    print("Local colours:", colour1)

print("Global color1:", colour1)

my_function2(colour1)

my_function2(colour1="gre") #DOES NOT WORK

'''Best practise is to create a GENERIC function like below, allowing you to pass amosth ANYTHING to the function'''

def my_function3(var):

    print("myfunc3 var:", var)

#notice the 3 ways of psasing any value/str to my_function3
my_function3("i have passed this str to the func :)")
my_function3(2)
my_function3(var="multicolor")
my_function3(["a","list"])

#-------------------------------------#
time.sleep(1)
print("\n")
print("----------A function to modify a list------------")

shopping_list=["apple","banana"]
def modify_list(shopping_list):
    shopping_list.append("orange")
    print("new shopping list:", shopping_list)

modify_list(shopping_list)

time.sleep(1)
print("\n")

print("----------Passing in arguments------------------")
    
'''If you have a function with many arguments it is easy to forget to enter them or you can enter them in the wrong order, hence, use args or kwargs. keyword arguments (KWARGS) preferred over positional arguments'''

def function_with_too_many_args(name, age, sex, city, role):
    print(name, age, sex, city, role)

function_with_too_many_args("bob",21,"M","London","coder")

'''This func has 5 input args! and invoking it is difficult as you have to pass in values for all 5 vars in the correct order. To solve this you should assign values using variable names rather than POSITION''' 

#Function with kwargs:
#my_function(var="x")

#A mix of positional arguments and kwargs

function_with_too_many_args("rob",21,"M",city="Ipswich",role="student")

#POSITIONAL args go first, followed by KWARGS in ANY ORDER
function_with_too_many_args("sam",32,role="developer",city="LA", sex="F")

#you can include DEFAULT VALUES for certain args, you can enter it in the , this can be overwritten by specifyig it but note this order:
'''Generally, non-default argument should not follow default argument , it means you can't define (a="b",c) in function.

The order of defining parameter in function are :

1.positional parameter or non-default parameter i.e (a,b,c)
2.keyword parameter or default parameter i.e (a="bcd",cifty="london")
3.keyword-only parameter i.e (*args)
4.var-keyword parameter i.e (**kwargs)'''

def another_function_with_many_args(name, age, sex, city="London"):
    print(name, age, sex, city)
    
another_function_with_many_args("jona",21,"M")

print("\n")
print("-----------First class functions----------------")
'''Since python functions are first class objects, you can assign them to variables, store them in data structures, pass them as arguments to other functions, and even return them as values from other functions.'''


def receipt(item1, item2):
    price = item1*item2
    return add_VAT(price)

def add_VAT(price):
    final = price*1.2
    return round(final)

calculate_total_price = receipt
print(calculate_total_price(2,3))

'''But you still musn't MISS ANY OUT.What if you have a func with variable no. of input vars?'''


    
    
    
    