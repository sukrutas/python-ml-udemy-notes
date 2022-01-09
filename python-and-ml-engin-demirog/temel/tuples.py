# WORKING WITH TUPLES

# like to list
# just one different things that can not change on it
# more effectively than list

# empty tuple
my_tuple = ()
print(my_tuple)

# tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [1,2,3], (4,5,6))
print(my_tuple)


tuplelist = (2,4,6, "Ankara",(2,3,4),[])
list1 = [2,4,6, "Ankara", [3,4,5],()]
list1[0] = 3

print(tuplelist[-2]) # reverse selecting
print(list1[-2])

print(tuplelist[1:2])
print(list1[1:2])

tuplelist2 = ("Adana",) # if tuple have one item you should put comma
print(type(tuplelist2))

print(type(tuplelist))
print(type(list1))
print(tuplelist)
print(list1)
print(len(tuplelist))
print(len(list1))
