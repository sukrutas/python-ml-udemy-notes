# WORKING WITH DICTIONARY

# like set it keep items as unordinary
# we can think dictionary in daily life

# empty dict
my_dict = {}

# dictionary with integer keys
my_dict = {1:'apple', 2:'ball'}

# dictionary with mixed keys
my_dict = {'name' : 'John', 1 : [2,3,4]}

# using dict()
my_dict = dict({1:'apple', 2 : 'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'),(2,'ball')])


dict1 = {
    "name" : "mehmet",
    "surname" : "yilmaz",
    "age" : 27
    }

print(dict1)

dict1["name"] = "sukru" # to change valeu of item
dict1["hometown"] = "bursa"
print(dict1)

dict2 = dict(name = "ayse", surname = "yilmaz")

del(dict2["surname"])
print(dict2)



