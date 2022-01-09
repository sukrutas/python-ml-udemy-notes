# WORKING WITH LISTS

# One of most using data types
# Ordinary and consisting index

# empty list
my_list = []

# list of integer
my_list = [1, 2, 3]

# list with mixed datatypes
my_list = [1, "Hello", 3.4]

# Also a list can even have another list as an item. This is called nested list

# nested list
my_list = ["mouse", [8,6,4], ['a']]


# ogrenci1 = "Engin"
# ogrenci2 = "Derin"
# ogrenci3 = "Salih"

# print(ogrenci1)
# print(ogrenci2)
# print(ogrenci3)

# to collect same place same or different datatypes datas

# to select
students= ["Engin", "Derin", "Salih"]
print(students[0])

print(students)
# to add
students.append("Sukru")
print(students)

# to remove 
students.remove("Sukru")
print(students)

# to replace
students[0] = "Sukru"
print(students)

# list constructor
cities = list(("Ankara", "Istanbul"))
print(cities)
print(len(cities))


# other functions

# print(cities.clear()) # clean the list

print("Count of Ankara : " + str(cities.count("Ankara"))) # count of item
print("Index of Ankara : " + str(cities.index("Ankara"))) # index of item 
cities.pop(1) # to remove item by index
cities.insert(1, "Istanbul") # to add item by index
print(cities)
cities.reverse() # to reverse list
print(cities)

# to back up
cities2 = cities.copy()
cities2.append("İzmir")
print(cities2)
print(cities)



























