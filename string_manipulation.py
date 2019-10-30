# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:08:13 2019

@author: rnikoo
"""
#-----Option 1 str.format()-----#

name = "jo"
age = 12

print("my name is {} and i'm {} years old".format(name,age))


# downside- can be quite verbose when you have multiple variables .format(var1,var2,var3...etc)


#-----Option 2 f-strings-----#
#see https://realpython.com/python-f-strings/#old-school-string-formatting-in-python

name = "rox"
age = 26

#F strings can be used with f or F, 
print(f"hi i'm {name} and {age}")

def fstrings_practise():
    name = input("what's your name?")
    age = input("how old are you?")
    print(f"Hi {name.title()}, nice to meet you!")
    
fstrings_practise()
    


#Define your variables

first_name = "Monty"
last_name = "Python"

full_name = first_name + " " + last_name

print(full_name)

#Function-based method for the above

def fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    print(full_name)
    
#Call the function with your arguments
fullname("john", "Brown")


#Now a superior version of fullname function automatically capitalising the name
def fullname_v2(*args):
    full_name = first_name.title() + " " + last_name.title()
    print(full_name)

fullname_v2("john", "Brown")

#--------------String INDEXING---------------#

word = "python"
#get the first letter
print(word[0])
new_word = word[0]+word[1]
print(new_word)
#print the slice from character 2 to 4
word_slice = word[1:4]
print(word_slice)

#--------------String SPLITTING---------------#

#uses the inbuilt .split() method

mystring="abacus will split"
print(mystring.split()) #will split tge word into its respective words

def split_sentence(sentence):
    split = sentence.split()
    return split

split_sentence("split me")

#
    