'''Given a number n, return the number of positive odd numbers below n, 

oddCount(7) //=> 3, i.e [1, 3, 5]'''

#Link to kata:   https://www.codewars.com/kata/count-odd-numbers-below-n/train/python 


#i added in an if statement so it only runs when the  number is odd e.g. if x/2 gives a remainder


def odd_count(n):
    if n %2 != 0:
        x = 1
        condition = x+2
        mylist=[1]
        while condition < n:
            #print(condition)
            mylist.append(condition)
            condition +=2
        return len(mylist)

odd_count(7)

#-------------------------#


def odd_count_spyder(n):
    if n %2 != 0:
        x = 1
        condition = x+2
        mylist=[1]
        while condition < n:
            #print(condition)
            mylist.append(condition)
            condition +=2
        print(mylist)
        print("number of positive odd number below n:", len(mylist))
    
odd_count_spyder(9)