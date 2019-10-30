# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:26:28 2019

@author: rnikoo
"""

def combine(a,b):
    result = a[0].append(b[0])
    return result
    
    
#combine([1,2],["a","b"])

#result = [1,"a",2,"b"]
def atest():
    list1=[1,2]
    listb=["a","b"]
    listc=[]
    for i in range(len(list1)):
        result = i + 2
        listc.append(result)
    print(listc)

#atest()

def atest2():
    list1=[1,2]
    listb=["a","b"]
    listc=[]
    for i in range(len(list1)):
        result = str(i) + listb[0]
        listc.append(result)
    print(listc)
    
#atest2()
    
#num_list = [1, 2, 3]
#alpha_list = ['a', 'b', 'c']
#newlist=[]
#for number in num_list:
#    newlist.append(number)
#    for letter in alpha_list:
#        newlist.append(letter)
#print(newlist)

def combine(num_list,alpha_list):
    print("numlist:", num_list)
    print("numlist:", alpha_list)
    newlist=[]
    for number in num_list:
        newlist.append(number)
        for letter in alpha_list:
            newlist.append(letter)
    print(newlist)
    
combine([1, 2, 3],['a', 'b', 'c'])
    