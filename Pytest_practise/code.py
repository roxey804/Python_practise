import random

class MyClass():

    def __init__(self):
        self.mydictionary={}
        #this creates an empty dictionary which will work as key:value pairs with name:number
    def add(self, name, number):
        self.mydictionary[name] = number
    def lookup(self, name):
        return self.mydictionary[name]
    def names(self):
        return self.mydictionary.keys()
        #return the keys which are names
    def numbers(self):
        return self.mydictionary.values()
        #return the values which are numbers

class Myclass:  
        
    def __init__(self, arg1, arg2):  
        self.arg1 = arg1  
        self.arg2 = arg2  
            
    def mymethod(self):  
        return "{} {}".format(self.arg1, self.arg2)  
	  
myvar = Myclass("this is arg 1", "this is arg2")   
	    
print(myvar.mymethod())  

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def credentials(self):
        return f'Hi im {self.name} and {self.age}'

jenny = Student("Jennifer", 21)
print(jenny.credentials())


def mytest():
    mylist = ['test1', 'position', 'string', 2]
    query = input("enter query")
    if query in mylist:
        return True
    else:
        return False
    
