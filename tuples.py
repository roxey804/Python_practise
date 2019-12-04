'''Tuples are like lists but IMmutable, hence, after creation you CANNOT append'''

my_tuple = (1,3,2)
print("my tuple:", my_tuple)
print("type:", type(my_tuple))

#You CANNOT assign/add/remove items to your tuple
#The .append() .remove() methods will NOT work on tuples, you will get an AttributeError "'tuple' object has no attribute 'method"
#but you CAN sort them

print("sorted(my_tuple) will work")

#you can convert other types into tuples yousing newvar = tuple(oldvar)

#---------Searching items in tuples---------#

fruit_tuple = ("banana", "orange", "apple")
#do you have an apple in your tuple?
#"apple" in fruit_tuple returns True
if "apple" in fruit_tuple:
    print("yes")