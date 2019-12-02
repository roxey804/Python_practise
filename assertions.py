#assert <condition> <"if not, print this>"

#assert len(mylist) != 0, "list is empty!"
'''assert the length of my list is NOT zero, if it IS zero (empty) print that statement '''

import time

def avg(marks):
    assert len(marks) != 0,"List is empty."
    print(sum(marks)/len(marks))


#([1])



def check_input():
    code = int(input("guess the code "))
    print("you entered: ", code)
    time.sleep(1)
    assert code == 123, "incorrect"
 
check_input()