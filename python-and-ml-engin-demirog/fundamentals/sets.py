# WORKING WITH SETS

# like to list
# it has not index
# it has unordinary items
# Items of sets must be unique
# More effectively than lists
# can not change on it but can add items

# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1,2,3)}
print(my_set)

# # using set func
# student_set2 = set("Mehmet","Veli","Ayşe")
# print(student_set2)

student_set = {"Engin", "Derin", "Salih"}
print(student_set)

for student in student_set:
    print(student)
    
print("Derin" in student_set)

if "Derin" in student_set:
    print("Listede var")

# to add    
student_set.add("Ali") # in list we use append func. but in set we use add func.
print(student_set)

# to update ('d like to item more than one)
student_set.update(["Mert", "Merve", "Ali"])
print(student_set)

print(len(student_set))

# to delete
student_set.remove("Mert")
print(student_set)

# to prevent error
student_set.discard("Mert")
print(student_set)

# # to delete items of set
# student_set.clear()
# print(student_set)

# # to delete set
# del student_set
# print(student_set)























