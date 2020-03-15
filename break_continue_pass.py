
"""
Break, Continue and Pass Python Keywords
"""

print("-------------Break, continue and pass keywords----------")

#When python encounters a BREAK keyword, it stops (the loop) and ceases code execution

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


print("-------Continue keyword---------")
time.sleep(1)   
#continue will skip execution of the remaining lines of code and go back to the if statement  

nums=[1,2,3,4,5,6,7,8,9]

for num in nums:
    if num % 2 ==0:
        continue
    print(num)
#this code will ignore the even numbers and print out odd no.s only
    
print("using continue to skip over a few items")
for i in nums:
    if i >=4 and i <=7:
        continue
    print(i)
