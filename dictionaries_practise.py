# -*- coding: utf-8 -*-
"""
Python dictionaries DO NOT have an inherent order, they are key:value pairs.
Keys must be UNIQUE
Dictionaries CANNOT contain lists as they are mutable
To print a value, use dictname["key"] e.g. mydict["name"]
"""

mydict = {
        "key1":"value1","key2":"value2","key3":None, "key4":123
        }

print("let's check the type")
print("type(mydict)", type(mydict))

students = [
        {"name":"Mark", "id":1},
        {"name":"Jenna", "id":2}
        ]

#------------------Extracting data from dictionaries--------------#
print("\n -------Extracting data from dictionaries-----")
print("Keys:", mydict.keys())
print("Values:", mydict.values())
print("this is the length of the dictionary: ", len(mydict))

print("\n -------Adding data to dictionaries----------")
#---------Adding data--------------#
#mydict[key] = "value"

def add_data():
    mydict["newkey"] = "newvalue"
    return mydict
#---------Modifying and deleting data--------------#
'''Dictionaries are IMmutable, hence changes will UPDATE/replace the entry and not create another version'''
def view_data():
    return mydict["key1"]
    
def modify_data():
    mydict["key4"] = 1234
    #the value for key4 will now be 1234

def delete_data():
    del(mydict["key5"])
    
def dict_length():
    return len(mydict)

print("\n -----is key x in this dictionary?------")
print(mydict)
print(" do: 'keyx' in dictname")
#"keyx" in mydict
#--------------using FOR loops ------------------#
    
def return_keys():
    for key in mydict:
        print(key)
        
def return_values():
    pass
    #for key,val in mydict.items():
        #print(val)

def return_kv_pairs():
    for item in mydict:
        print(item, mydict[item])
       #print(item, ":", mydict[item])

#or def print_kv_pairs():
    #for key,val in mydict.items():
        #print(key, val)
        
#------------Searching in a dictionary------------------------#

def get_value_for_key():
    mykey = input("enter key searching for:")
    if mydict[mykey] == None:
        print(mykey, "has no value")
    return mydict[mykey]


#--------tests for dictionary errors-----------#    

def test_mydict():
    mydict["testkey"] = "testvalue"
    assert mydict["testkey"] == "testvalue"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
