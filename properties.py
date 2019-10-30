# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:15:22 2019

@author: rnikoo
"""

class Employee:
    
    def __init__(self, first, last,salary):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.salary ="£" + salary
    
        
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def credentials(self):
        return f"{self.first.title()} {self.last.title()}, {self.email}, salary: {self.salary}"
    
     
emp_1 = Employee("john", "smith", "30000")
emp_2 = Employee("sara", "doe", "40000")

#print(emp_1.email) #does not need ()  as an instance? of the class
#print(emp_1.last)
#print(emp_1.salary)
#print(emp_1.credentials(),"\n", emp_2.credentials()) #needs () for the method

#emp_1.first = "Newbie"
#
#print(emp_1.first)
#print(emp_1.email)
#print(emp_1.fullname())

#note now the email does not update! 

#This can be fixed using the @property DECORATOR

#-----------------Decorators: @propert, getter and setter methods---------------#


#Now with PROPERTY decorators allowinG you to DEFINE a method and access it like an ATTRIBUTE
#so like a self.etc


class Employee_with_decorators:
    
    def __init__(self, first, last,salary):
        self.first = first
        self.last = last
#        self.email = first + "." + last + "@email.com"
        self.salary ="£" + salary
        
    @property #allows us to access email as an ATTRIBUTE
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    @property   
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ") #will split line 75
        self.first = first
        self.last = last
    
    def credentials(self):
        return f"{self.first.title()} {self.last.title()}, {self.email}, salary: {self.salary}"
    
     
emp_1 = Employee_with_decorators("john", "smith", "30000")
emp_1.fullname = "corey schafer"

print(emp_1.email) #note no brackets after the method now
print(emp_1.fullname) #will give Can't set attribute error

#we must now change fullname to a setter 



    
    
    