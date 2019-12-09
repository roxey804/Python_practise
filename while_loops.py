import time

#--------WHILE Loops ---------#

'''Repeat this action until the condition is no longer satisfied'''


#while condition:   while True / while False
    #expression

# while condition:
#     pass

#code
# while condition:
#     pass
# #more code

print("-------------While True loops----------")


#while True:
#    ("this is an infinite loop")
    
'''While True loops will run infinitely, hence they need to be explicitl TERMINATED'''

error=50
while error >1:
    error = error/4 #you MUST UPDATE the error var!
    print(error)

'''Steps for creating a while loop that will not run indefinitely'''

#1. Assign myvar a value
#2. add a while statement with a condition (e.g. equal to, greater than/less than)
#3. update myvar

print("Example while loop")

myvar = 7

while myvar == 7:
    print(myvar)
    myvar = myvar*2
    
number=45

print("while loop incrementing by +2 every time")
while number<50:
    print(number)
    number = number +2
#the While loop will terminate once number = 49
    
is_positive = 10

while is_positive > 0:
    print(is_positive, "is still positive")
    is_positive -= 3
#note to deduct and reassign the var you must use -=

print("-------------While False loops----------")

while False:
    ("this will never be printed")

colour=input("guess my favourite colour?")
while colour != "blue":
    print("Wrong, try again!")
    colour=input("guess my favourite colour?")
print("correct! my favourite colour is", colour)

#remember to also include the input statement INSIDE your while loop!

print("-------------Break, continue and pass keywords----------")
#at BREAK python stops the loop and ceases code execution

mylist = [1,2,3]
for item in mylist:
    print(item)
    break
#this will STOP the loop after the first item in the list.
    
print("Checking if we have an item in our list")

holiday_bag=["passport","money","phone"]
#Check if you've got your phone:
for item in holiday_bag:
    if item =="phone":
        print("found the phone!")
        break

time.sleep(1)
for item in holiday_bag:
    if item =="phone":
        print("found the phone!")
        break
    print("other items:", item)
    
print("-----Is there any no. divisible by 3 in our list?----")

numlist = [1,2,3,4,5,7,8,9]

for num in numlist:
    if num % 3 == 0:
        print(num, "is divisible by 3")
        break
    print(num, "not a multiple of 3")   
#BUT 9 will not be found! hence, we need to use continue
    
#continue will skip execution of the remaining lines of code and go back to the if statement  
    
    
